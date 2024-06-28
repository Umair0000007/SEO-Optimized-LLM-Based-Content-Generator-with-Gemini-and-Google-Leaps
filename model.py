import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

def load_model(title, head1, head2):
    google_api_key = os.getenv("Google_API_KEY")
    genai.configure(api_key=google_api_key)
    prompt = (f"I will provide you with a list of blog titles, H1 headings, and H2 headings. "
              f"Analyze these lists, ignore unnecessary items, and generate an article structure for me. "
              f"Titles: {title}, H1: {head1}, H2: {head2}")
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(prompt)
    return response.text
