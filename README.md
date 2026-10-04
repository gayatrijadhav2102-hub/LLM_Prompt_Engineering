# AI Study Assistant 🤖

An AI-powered study assistant built using **Python and Google's Gemini API**.  
This project demonstrates how to integrate an LLM into a Python application and use prompt engineering to create an interactive AI assistant.

## 🚀 Features

- Interactive AI chatbot
- AI-based study assistance
- Ask questions about technical topics
- Simple and beginner-friendly explanations
- Prompt engineering using Role, Task, Context, Format, and Constraints
- Environment variable support for API keys
- Git/GitHub version control

## 🛠️ Technologies Used

- Python
- Google Gemini API
- Google GenAI Python SDK
- python-dotenv
- Git
- GitHub

## 📁 Project Structure

```text
AI-Study-Assistant/
│
├── main.py
├── requirements.txt
├── .gitignore
└── .env
```

> `.env` is not committed to GitHub because it contains the Gemini API key.

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd AI-Study-Assistant
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 🔑 Configure Gemini API

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

Never commit the `.env` file to GitHub.

## ▶️ Run the Application

```bash
python main.py
```

Example:

```text
AI Study Assistant started. Type 'exit' to stop.

You: What is RAG?

AI: RAG stands for Retrieval-Augmented Generation...
```

Type:

```text
exit
```

to stop the application.

## 🧠 Prompt Engineering

The application uses prompt engineering to control the behavior of the AI.

Example:

```text
ROLE:
You are an AI Study Assistant.

TASK:
Help the student understand technical concepts.

CONTEXT:
The student is preparing for a Python and GenAI interview.

FORMAT:
Explain the concept using:
1. Definition
2. Explanation
3. Example

CONSTRAINTS:
Keep the explanation simple and beginner-friendly.
```

## 🔄 Application Flow

```text
User
  ↓
Python Application
  ↓
Create Prompt
  ↓
Gemini API
  ↓
Gemini LLM
  ↓
Generated Response
  ↓
Display Response
```

## 📚 Concepts Practiced

During this practical, I learned:

- What is an LLM
- Gemini API
- Google GenAI SDK
- API keys and `.env`
- `client`
- `client.interactions.create()`
- Model selection
- Input and output tokens
- Prompt engineering
- Role-based prompting
- AI chatbot development


## 🔮 Future Improvements

- Add conversation memory
- Add PDF/document upload
- Implement RAG
- Add embeddings and vector database
- Generate quizzes and MCQs
- Generate flashcards
- Add study progress tracking
- Build FastAPI backend
- Build React frontend
- Store user data in PostgreSQL

## 👩‍💻 Learning Goal

This project is part of my practical learning journey in **Python, Generative AI, LLMs, Prompt Engineering, RAG, and AI application development**.
