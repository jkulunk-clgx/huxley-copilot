from app import create_app

# We call the factory function we wrote in the app/__init__.py file to create our Flask app instance.
# This 'app' variable is the actual application object that the server will run.
app = create_app()

if __name__ == "__main__":
    # This block only runs if you execute this file directly (e.g., 'python run.py').
    # It starts the Flask development server on port 5001.
    # debug=True allows the server to auto-reload when you save changes and provides helpful error messages in the browser.
    app.run(debug=True, port=5001)