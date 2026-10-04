import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GENAI_API_KEY")
client = genai.Client(api_key=api_key)

topic  = input("Enter a topic for the study assistant: ")
level = input("Enter the current level (beginner, intermediate, advanced): ")
prompt = f"""
Act as a trainer. 
Teach me about {topic}

student Level:
{level}

use this format:
1. simple definition
2. Real-life examples
3. step-by-step explanation
4. common mistakes to avoid
5. 4 quiz questions
6. short summary

use Easy laguage and avoid technical jargon.

"""

response = client.interactions.create(
    model="gemini-3.5-flash",
    input=prompt,
)

print(response.output_text)
