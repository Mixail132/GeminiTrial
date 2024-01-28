import os
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")
os.environ['GOOGLE_API_KEY'] = API_KEY


import google.generativeai as genai
model = genai.GenerativeModel("gemini-pro")


def gemini_ai(prompt):
    prompt = prompt
    response = model.generate_content(contents=[prompt])
    return response.text
