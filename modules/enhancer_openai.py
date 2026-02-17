import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Use Gemini 2.5 Flash (best choice)
model = genai.GenerativeModel("models/gemini-2.5-flash")


def enhance_resume(text):

    if not text:
        return "No resume content found."

    prompt = f"""
    You are an expert resume writer.

    Improve this resume professionally and optimize it for ATS systems.

    Improve:
    - Professional wording
    - Grammar
    - Impact
    - ATS keywords
    - Clarity

    Resume:
    {text}
    """

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"Gemini Error: {str(e)}"
