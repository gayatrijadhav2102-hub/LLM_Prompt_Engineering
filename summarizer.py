import os
from dotenv import load_dotenv
from google import genai

# 1. Load environment variables
load_dotenv()

# 2. Get API key
api_key = os.getenv("GEMINI_API_KEY")

# 3. Create Gemini client
client = genai.Client(api_key=api_key)

# 4. Text to summarize
text = """
Python is a high-level, interpreted programming language known for
its simple and readable syntax. It is widely used in web development,
data science, artificial intelligence, automation, and scripting.

Python supports multiple programming paradigms, including procedural,
object-oriented, and functional programming. It also has a large
standard library and a huge ecosystem of third-party packages.

Because of its simplicity and flexibility, Python is one of the most
popular programming languages for beginners as well as experienced
developers.
"""

# 5. Role
role = """
You are an expert summarizer.
"""

# 6. Task
task = """
Summarize the given text.
"""

# 7. Context
context = """
The summary is for a software developer who wants to
quickly understand the main points.
"""

# 8. Format
format = """
Return the summary in this format:

Title:
<short title>

Summary:
<short paragraph>

Key Points:
- Point 1
- Point 2
- Point 3
"""

# 9. Constraints
constraints = """
Rules:
- Keep the summary concise.
- Include only important information.
- Do not add information that is not present in the original text.
- Keep the summary under 100 words.
"""

# 10. Create the complete prompt
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

TEXT TO SUMMARIZE:
{text}
"""

# 11. Send request to Gemini
response = client.interactions.create(
    model="gemini-3.5-flash-lite",
    input=prompt
)

# 12. Print result
print(response.output_text)