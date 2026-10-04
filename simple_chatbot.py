import os
from dotenv import load_dotenv
from google import genai

# 1. Load environment variables
load_dotenv()

# 2. Get API key
api_key = os.getenv("GEMINI_API_KEY")

# 3. Create Gemini client
client = genai.Client(api_key=api_key)

print("AI chatbot started. Type 'exit' to stop the conversation.")

while True:
    # 4. Get user input
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Exiting the chatbot. Goodbye!")
        break

    # 5. Create prompt for the chatbot
    prompt = f"""
    You are a helpful AI chatbot. 
    Respond to the user's message in a friendly and informative manner.

    User: {user_input}
    """

    # 6. Send request to Gemini
    response = client.interactions.create(
    model="gemini-3.5-flash", 
    # instruction="You are a helpful AI chatbot. Respond to the user's message in a friendly and informative manner.",
    input=prompt)

    # 7. Print the chatbot's response
    print(f"AI: {response.output_text}")
