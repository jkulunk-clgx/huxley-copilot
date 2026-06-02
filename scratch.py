from google import genai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    print("No key")
    exit()

client = genai.Client(api_key=api_key)
try:
    response = client.models.generate_content(
        model='gemini-2.0-flash-thinking-exp-01-21',
        contents='What is 2+2? Think about it.',
    )
    for part in response.candidates[0].content.parts:
        print(f"Thought? {part.thought}: {part.text[:50]}...")
except Exception as e:
    print("Error:", e)
