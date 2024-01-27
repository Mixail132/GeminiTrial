import os
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")
os.environ['GOOGLE_API_KEY'] = API_KEY
import google.generativeai as genai
model = genai.GenerativeModel("gemini-pro")
prompt = "Is that correct name? Agata Kristie"
response = model.generate_content(contents=[prompt])
print(response.text)
