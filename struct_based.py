import os
from dotenv import load_dotenv
from google import genai

# 1. Load environment variables
load_dotenv()

# 2. Get API key
api_key = os.getenv("GEMINI_API_KEY")

# 3. Create Gemini client
client = genai.Client(api_key=api_key)

# 4. Define the role
role = """
You are a senior Python technical interviewer.
"""

# 5. Define the task
task = """
Ask the candidate one Python interview question.
"""

# 6. Define the context
context = """
The candidate has around 3 years of Python development experience
and is preparing for a Python GenAI Developer interview.
"""

# 7. Define the format
format = """
Return the response in this format:

Question:
<interview question>

What the interviewer is testing:
<concept being tested>
"""

# 8. Define the constraints
constraints = """
Rules:
- Ask only one question.
- Do not provide the answer.
- Start with a basic Python question.
- Keep the question clear and concise.
- Do not repeat questions.
"""

# 9. Combine everything into one prompt
prompt = f"""
ROLE:
{role}

TASK:
{task}

CONTEXT:
{context}

FORMAT:
{format}

CONSTRAINTS:
{constraints}
"""

# 10. Send prompt to Gemini
response = client.interactions.create(model="gemini-3.5-flash-lite", input=prompt)

# 11. Print Gemini's response
print(response.output_text)
