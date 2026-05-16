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
                    # Retrieve all RAG files from the registry
                    rag_contexts = []
                    for key, rag_file_path in RAG_REGISTRY.items():
                        if rag_file_path and os.path.exists(rag_file_path):
                            with open(rag_file_path, 'r', encoding='utf-8') as f:
                                rag_contexts.append(f"--- {key} ---\n{f.read()}")
                    
                    rag_context = "\n\n".join(rag_contexts)

                    # Bundle the RAG context with the user's request
                    if rag_context:
                        combined_prompt = f"Context from RAG files:\n{rag_context}\n\nUser Request:\n{user_input}"
                    else:
                        combined_prompt = user_input

                    client = genai.Client()
                    response = client.models.generate_content(
                        model='gemini-3-flash-preview',
                        contents=combined_prompt
                    )
                    ai_response = response.text
                    
                    # Print token counts to the terminal so developers can monitor API usage and costs.
                    # response.usage_metadata contains information about how many tokens were used.
                    if response.usage_metadata:
                        print(f"Input Token Count: {response.usage_metadata.prompt_token_count}")
                        print(f"Output Token Count: {response.usage_metadata.candidates_token_count}")
                except Exception as e:
                    error_message = f"An error occurred: {str(e)}"

            if request.is_json:
                return jsonify({'ai_response': ai_response, 'error_message': error_message})

        return render_template('index.html', ai_response=ai_response, error_message=error_message, user_input=user_input)

    return app
