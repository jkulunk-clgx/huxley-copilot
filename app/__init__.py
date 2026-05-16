import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from google import genai

# RAG_REGISTRY is a dictionary that maps descriptive keys (like "system_instructions") 
# to the actual file paths of Markdown documents. We use this to easily find and load 
# these files later when we need to add their content as context for the AI.
RAG_REGISTRY = {
    "default": "rag_data/registry.md",
    "system_instructions": "rag_data/system_instructions.md",
    "persona_format": "output_formats/persona_format.json",
    "JTBD_format": "output_formats/JTBD_format.json",
    "journey_map_format": "output_formats/journey_map_format.json",
    "data": "rag_data/Data-Real-Estate-Agent-001.md"
}

def create_app():
    """
    This is the application factory function. 
    It creates and configures the Flask application instance.
    Using a factory function is a best practice because it allows you to create 
    multiple instances of the app (e.g., for testing) without global state issues.
    """
    app = Flask(__name__)

    @app.route('/check_intent', methods=['POST'])
    def check_intent():
        user_input = request.json.get('user_input') if request.is_json else None
        notification_message = None
        role = None
        error_message = None
        
        load_dotenv()
        api_key = os.environ.get("GEMINI_API_KEY")
        if not api_key or api_key == "your_api_key_here":
            error_message = "Gemini API key is missing. Please set it in the .env file."
        elif user_input:
            try:
                client = genai.Client()
                extraction_prompt = f"Extract the target user role from this user request: '{user_input}'. Return only the role name in snake_case (e.g. data_scientist, mortgage_lender), or 'None' if no role is specified."
                role_response = client.models.generate_content(
                    model='gemini-3-flash-preview',
                    contents=extraction_prompt
                )
                role = role_response.text.strip().lower()
                
                if role and role != "none":
                    expected_rag_file = f"rag_data/Data-{role.replace('_', '-')}.md"
                    if not os.path.exists(expected_rag_file):
                        expected_raw_file = f"raw_data/transcript_{role}.md"
                        if os.path.exists(expected_raw_file):
                            notification_message = f"I noticed we don't have structured data on {role.replace('_', ' ').title()}. I will now process the raw transcript and add it to our knowledge base. This may take a moment..."
                        else:
                            notification_message = f"I couldn't find any real data for {role.replace('_', ' ').title()}. I will generate a synthetic knowledge base using AI training data before proceeding. Please note this data is unvalidated."
            except Exception as e:
                error_message = f"An error occurred: {str(e)}"
                
        return jsonify({'role': role, 'notification': notification_message, 'error_message': error_message})

    @app.route('/', methods=['GET', 'POST'])
    def index():
        """
        This function handles requests to the root URL ('/').
        - On a GET request (when a user visits the page), it simply renders the index.html template.
        - On a POST request (when a user submits the chat form), it takes the user's input,
          loads the RAG (Retrieval-Augmented Generation) files to provide context, 
          sends everything to the Gemini AI model, and then returns the AI's response to the template.
        """
        ai_response = None
        error_message = None
        user_input = None
        notification_message = None

        if request.method == 'POST':
            if request.is_json:
                user_input = request.json.get('user_input')
            else:
                user_input = request.form.get('user_input')
            
            # Load env here in case they added the key after starting the server
            load_dotenv()
            api_key = os.environ.get("GEMINI_API_KEY")

            if not api_key or api_key == "your_api_key_here":
                error_message = "Gemini API key is missing. Please set it in the .env file."
            elif user_input:
                try:
                    client = genai.Client()
                    
                    role = None
                    if request.is_json:
                        role = request.json.get('role')
                        
                    if not role:
                        # Phase 1: Intent & Role Extraction (Fallback)
                        extraction_prompt = f"Extract the target user role from this user request: '{user_input}'. Return only the role name in snake_case (e.g. data_scientist, mortgage_lender), or 'None' if no role is specified."
                        role_response = client.models.generate_content(
                            model='gemini-3-flash-preview',
                            contents=extraction_prompt
                        )
                        role = role_response.text.strip().lower()
                    
                    # Phase 2: Raw Data Ingestion (Conditional)
                    if role and role != "none":
                        expected_rag_file = f"rag_data/Data-{role.replace('_', '-')}.md"
                        if not os.path.exists(expected_rag_file):
                            expected_raw_file = f"raw_data/transcript_{role}.md"
                            if os.path.exists(expected_raw_file):
                                with open("rag_data/registry.md", 'r', encoding='utf-8') as f:
                                    registry_content = f.read()
                                with open(expected_raw_file, 'r', encoding='utf-8') as f:
                                    raw_content = f.read()
                                    
                                ingestion_prompt = f"{registry_content}\n\n---\n\nRaw Transcript to process:\n{raw_content}"
                                processed_response = client.models.generate_content(
                                    model='gemini-3-flash-preview',
                                    contents=ingestion_prompt
                                )
                                
                                with open(expected_rag_file, 'w', encoding='utf-8') as f:
                                    f.write(processed_response.text)
                            else:
                                with open("rag_data/registry.md", 'r', encoding='utf-8') as f:
                                    registry_content = f.read()
                                    
                                synthetic_prompt = f"Using your internal training data, create highly detailed, realistic user interview insights for a '{role.replace('_', ' ')}'. You MUST strictly follow the exact Markdown template and schema provided below. Do not output anything outside the schema.\n\nHere is the schema:\n\n{registry_content}"
                                processed_response = client.models.generate_content(
                                    model='gemini-3-flash-preview',
                                    contents=synthetic_prompt
                                )
                                
                                warning_banner = "> [!WARNING]\n> **UNVALIDATED SYNTHETIC DATA**\n> This knowledge base was generated from AI training data because no raw interview transcripts were found for this role.\n\n"
                                
                                with open(expected_rag_file, 'w', encoding='utf-8') as f:
                                    f.write(warning_banner + processed_response.text)

                    # Phase 3: Artifact Generation & Fulfillment
                    rag_contexts = []
                    for key, rag_file_path in RAG_REGISTRY.items():
                        if rag_file_path and os.path.exists(rag_file_path):
                            with open(rag_file_path, 'r', encoding='utf-8') as f:
                                rag_contexts.append(f"--- {key} ---\n{f.read()}")
                                
                    import glob
                    for file_path in glob.glob("rag_data/Data-*.md"):
                        if file_path not in RAG_REGISTRY.values():
                            with open(file_path, 'r', encoding='utf-8') as f:
                                rag_contexts.append(f"--- dynamically_loaded_{os.path.basename(file_path)} ---\n{f.read()}")
                    
                    rag_context = "\n\n".join(rag_contexts)

                    if rag_context:
                        combined_prompt = f"Context from RAG files:\n{rag_context}\n\nUser Request:\n{user_input}"
                    else:
                        combined_prompt = user_input

                    response = client.models.generate_content(
                        model='gemini-3-flash-preview',
                        contents=combined_prompt
                    )
                    ai_response = response.text
                    
                    if response.usage_metadata:
                        print(f"Input Token Count: {response.usage_metadata.prompt_token_count}")
                        print(f"Output Token Count: {response.usage_metadata.candidates_token_count}")
                except Exception as e:
                    error_message = f"An error occurred: {str(e)}"

            if request.is_json:
                return jsonify({'ai_response': ai_response, 'error_message': error_message, 'notification': notification_message})

        return render_template('index.html', ai_response=ai_response, error_message=error_message, user_input=user_input, notification=notification_message)

    return app
