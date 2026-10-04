import os
from dotenv import load_dotenv
from google import genai

# Load .env file
load_dotenv()

# Get API key
api_key = os.getenv("GEMINI_API_KEY")

# Create Gemini client
client = genai.Client(api_key=api_key)

# Requirement provided by QA
requirement = """
The user should be able to log in using a valid email and password.
If the email or password is incorrect, an appropriate error message
should be displayed.
"""

# Prompt
prompt = f"""
ROLE:
You are an experienced QA engineer.

TASK:
Generate test cases for the given software requirement.

FORMAT:
Return the test cases in this format:

Test Case ID:
Test Scenario:
Preconditions:
Test Steps:
Expected Result:
Test Type:

CONSTRAINTS:
- Generate positive and negative test cases.
- Include boundary/validation cases where applicable.
- Do not invent features that are not mentioned in the requirement.
- Generate 2 test cases.

REQUIREMENT:
{requirement}
"""

# Call Gemini
response = client.interactions.create(model="gemini-3.5-flash-lite", input=prompt)

# Display generated test cases
print("\n===== GENERATED TEST CASES =====\n")
print(response.output_text)
