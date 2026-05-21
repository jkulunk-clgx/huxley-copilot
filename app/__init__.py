import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from app.ai_service import generate_ai_response, extract_role_from_input

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
                role = extract_role_from_input(user_input, api_key)
                
                if role and role != "none":
                    expected_rag_file = f"rag_data/Data-{role.replace('_', '-')}.md"
                    if not os.path.exists(expected_rag_file):
                        expected_raw_file = f"raw_data/transcript_{role}.md"
                        if os.path.exists(expected_raw_file):
                            notification_message = f"I noticed we don't have structured data on {role.replace('_', ' ').title()}. I will now process the raw transcript and add it to our knowledge base. This may take a moment..."
                        else:
                            notification_message = f"I couldn't find any real data for {role.replace('_', ' ').title()}. I will perform a web-lookup to gather up-to-date information before proceeding."
                    else:
                        notification_message = f"I am referencing the existing data for {role.replace('_', ' ').title()} to generate this artifact."
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
                role = None
                if request.is_json:
                    role = request.json.get('role')
                ai_response, notification_message, error_message = generate_ai_response(user_input, role, api_key)

            if request.is_json:
                return jsonify({'ai_response': ai_response, 'error_message': error_message, 'notification': notification_message})

        return render_template('index.html', ai_response=ai_response, error_message=error_message, user_input=user_input, notification=notification_message)

    return app
