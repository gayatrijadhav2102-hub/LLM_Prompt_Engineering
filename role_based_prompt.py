import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

prompt = """
You are a senior Python developer and interview coach.

Explain Python decorators to me in one sentence.
I have 2 years of Python experience.
Explain the concept simply and give one practical example.
"""

response = client.interactions.create(model="gemini-3.5-flash-lite", input=prompt)

print(response.output_text)
