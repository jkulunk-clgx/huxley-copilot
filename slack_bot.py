import os
import tempfile
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from dotenv import load_dotenv
from app.ai_service import generate_ai_response

load_dotenv()

# Initialize your app with your bot token and socket mode handler
app = App(token=os.environ.get("SLACK_BOT_TOKEN"))

@app.event("app_mention")
def handle_app_mention_events(body, say, client):
    event = body.get("event", {})
    user = event.get("user")
    text = event.get("text", "")
    channel_id = event.get("channel")
    ts = event.get("ts")
    
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
    
    # Only respond to direct messages here, app_mention handles channels
    if channel_type == "im" and not event.get("bot_id"):
        user_input = event.get("text", "").strip()
        user = event.get("user")
        channel_id = event.get("channel")
        ts = event.get("ts")
        
        process_message(user_input, user, channel_id, ts, client, say)

pending_confirmations = {}

def process_message(user_input, user, channel_id, ts, client, say):
    global pending_confirmations
    state_key = f"{channel_id}_{user}"
    
    if state_key in pending_confirmations:
        if user_input.lower().strip() in ["yes", "proceed", "y", "sure", "ok", "yeah"]:
            original_input = pending_confirmations[state_key]
            del pending_confirmations[state_key]
            say(text=f"Hi <@{user}>, proceeding with the web search...", thread_ts=ts)
            api_key = os.environ.get("GEMINI_API_KEY")
            ai_response, notification_message, error_message, _ = generate_ai_response(original_input, api_key=api_key, allow_web_search=True)
        else:
            del pending_confirmations[state_key]
            say(text=f"Okay, request cancelled.", thread_ts=ts)
            return
    else:
        say(text=f"Hi <@{user}>, I'm thinking about that...", thread_ts=ts)
        
        api_key = os.environ.get("GEMINI_API_KEY")
        ai_response, notification_message, error_message, needs_permission = generate_ai_response(user_input, api_key=api_key, allow_web_search=False)
        
        if needs_permission:
            pending_confirmations[state_key] = user_input
    
    if error_message:
        say(text=f"Sorry, I ran into an error: {error_message}", thread_ts=ts)
        return
        
    if notification_message:
        say(text=f"{notification_message}", thread_ts=ts)
        
    if ai_response:
        # Create a temporary markdown file to upload
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.md', prefix='response_') as temp_file:
            temp_file.write(ai_response)
            temp_file_path = temp_file.name
            
        try:
            # Upload the file
            client.files_upload_v2(
                channel=channel_id,
                thread_ts=ts,
                file=temp_file_path,
                title="Huxley Response",
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
