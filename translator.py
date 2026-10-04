import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

sentence = "Prompt engineering is the process of designing and refining prompts to effectively communicate with AI models, ensuring they generate desired outputs."

prompt = f"""
    Translate the following sentence into Marathi
    {sentence}

    """

response = client.interactions.create(model="gemini-3.5-flash-lite", input=prompt)

print(response.output_text)