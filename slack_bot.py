import os
import re
import tempfile
import glob
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from dotenv import load_dotenv
from app.ai_service import generate_ai_response, extract_role_from_input

load_dotenv()

# Initialize your app with your bot token and socket mode handler
app = App(token=os.environ.get("SLACK_BOT_TOKEN"))

@app.event("app_mention")
def handle_app_mention_events(body, say, client):
    event = body.get("event", {})
    user = event.get("user")
    text = event.get("text", "")
    channel_id = event.get("channel")
    ts = event.get("thread_ts", event.get("ts"))
    
    # Strip the mention from the text
    # text looks like "<@U123456> I need a persona"
    if ">" in text:
        user_input = text.split(">", 1)[1].strip()
    else:
        user_input = text.strip()
        
    process_message(user_input, user, channel_id, ts, client, say)

@app.event("message")
def handle_message_events(body, say, client):
    event = body.get("event", {})
    channel_type = event.get("channel_type")
    
    user = event.get("user")
    channel_id = event.get("channel")
    state_key = f"{channel_id}_{user}"
    
    # Respond to direct messages, OR if the user has a pending confirmation in this channel
    if not event.get("bot_id"):
        if channel_type == "im" or state_key in pending_confirmations:
            user_input = event.get("text", "").strip()
            ts = event.get("thread_ts", event.get("ts"))
            
            process_message(user_input, user, channel_id, ts, client, say)

pending_confirmations = {}

def get_filename_from_markdown(markdown_text):
    filename = 'download.md'
    match = re.search(r'^#{1,4}\s+(.+)$', markdown_text, re.MULTILINE)
    if match:
        title = match.group(1).strip()
        words = title.split()[:5]
        title = '-'.join(words)
        title = title.lower()
        title = re.sub(r'[^a-z0-9-]', '', title)
        title = re.sub(r'-+', '-', title).strip('-')
        if title:
            filename = f"{title}.md"
    return filename

def process_message(user_input, user, channel_id, ts, client, say):
    global pending_confirmations
    state_key = f"{channel_id}_{user}"
    
    if state_key in pending_confirmations:
        if user_input.lower().strip() in ["yes", "proceed", "y", "sure", "ok", "yeah"]:
            state_data = pending_confirmations[state_key]
            if isinstance(state_data, dict):
                original_input = state_data['user_input']
                role = state_data.get('role')
            else:
                original_input = state_data
                role = None
            del pending_confirmations[state_key]
            
            def slack_notify_confirm(msg):
                say(text=msg, thread_ts=ts)
                
            slack_notify_confirm(f"Hi <@{user}>, proceeding with the web search...")
            api_key = os.environ.get("GEMINI_API_KEY")
            ai_response, notification_message, error_message, _ = generate_ai_response(
                original_input, role=role, api_key=api_key, allow_web_search=True, notify_callback=slack_notify_confirm
            )
        else:
            del pending_confirmations[state_key]
            say(text=f"Okay, request cancelled.", thread_ts=ts)
            return
    else:
        def slack_notify(msg):
            say(text=msg, thread_ts=ts)
            
        slack_notify(f"Hi <@{user}>, I'm thinking about that...")
        
        api_key = os.environ.get("GEMINI_API_KEY")
        if not api_key or api_key == "your_api_key_here":
            say(text=f"Gemini API key is missing. Please set it in the .env file.", thread_ts=ts)
            return
            
        try:
            role = extract_role_from_input(user_input, api_key)
            
            notification_message = None
            needs_permission = False
            
            if role and role != "none":
                search_pattern = role.replace("_", "-").lower()
                found_rag_file = None
                for file_path in glob.glob("rag_data/Data-*.md"):
                    if search_pattern in os.path.basename(file_path).lower():
                        found_rag_file = file_path
                        break
                        
                if not found_rag_file:
                    expected_raw_file = f"raw_data/transcript_{role}.md"
                    if not os.path.exists(expected_raw_file):
                        needs_permission = True
                        notification_message = f"I couldn't find any real data for {role.replace('_', ' ').title()}. Should I proceed with an internet search? Please note that any data returned will not be validated. Reply 'yes' to proceed."
            
            if needs_permission:
                say(text=f"{notification_message}", thread_ts=ts)
                pending_confirmations[state_key] = {'user_input': user_input, 'role': role}
                return
                
            ai_response, _, error_message, _ = generate_ai_response(
                user_input, role=role, api_key=api_key, allow_web_search=False, notify_callback=slack_notify
            )
                
        except Exception as e:
            error_message = f"An error occurred: {str(e)}"
            ai_response = None
            
    if error_message:
        say(text=f"Sorry, I ran into an error: {error_message}", thread_ts=ts)
        return
        
    if ai_response:
        filename = get_filename_from_markdown(ai_response)
        
        # Create a temporary markdown file to upload
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.md') as temp_file:
            temp_file.write(ai_response)
            temp_file_path = temp_file.name
            
        try:
            # Upload the file
            client.files_upload_v2(
                channel=channel_id,
                thread_ts=ts,
                file=temp_file_path,
                filename=filename,
                title=filename.replace('.md', '').replace('-', ' ').title(),
                initial_comment=f"Here is your generated response, <@{user}>!"
            )
        except Exception as e:
            say(text=f"Failed to upload the file: {e}", thread_ts=ts)
        finally:
            os.remove(temp_file_path)

if __name__ == "__main__":
    app_token = os.environ.get("SLACK_APP_TOKEN")
    if not app_token or app_token == "xapp-your-app-token-here":
        print("SLACK_APP_TOKEN is missing or invalid. Please set it in .env")
        exit(1)
        
    bot_token = os.environ.get("SLACK_BOT_TOKEN")
    if not bot_token or bot_token == "xoxb-your-bot-token-here":
        print("SLACK_BOT_TOKEN is missing or invalid. Please set it in .env")
        exit(1)
        
    print("Starting Huxley Slack Bot in Socket Mode...")
    SocketModeHandler(app, app_token).start()
