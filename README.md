# Multi-Model-LLM-Prompt-Service
This is a minimal Python-based chatbot service that integrates multiple open-source large language models (LLMs) and exposes them via a simple Streamlit interface. It supports model switching, prompt/response logging (latency and token count), and is built for rapid prototyping of LLM comparison tasks.

# Features
Query open-source LLMs (e.g., Gemma, LLaMA) using a unified interface

Switch between models dynamically using a dropdown

View responses in JSON format

Log latency and token usage for each prompt/response

Save logs in both CSV and JSON formats

Clean and minimal Streamlit frontend

# Project Structure

├── app.py                     # Main application script (Streamlit)

├── requirements.txt           # Python dependencies

├── .env                       # Environment variables for API keys

├── logs/

│   ├── prompt_logs.csv        # Logged prompts (CSV)

│   └── prompt_logs.json       # Logged prompts (JSON)


# Setup & Installation

1. Clone the Repository

git clone https://github.com/your-username/llm-multi-model-service.git
cd llm-multi-model-service

2. Create and Activate a Virtual Environment

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install Dependencies
pip install -r requirements.txt

4. Set Up Environment Variables
Create a .env file in the root directory with the following contents:
GROQ_API_KEY=your-groq-api-key
LANGCHAIN_API_KEY=your-langchain-api-key

# Run the App
streamlit run app.py

# Usage
Select a model from the sidebar dropdown

Type a question in the text box

View:

JSON response

Automatically saved logs (logs/prompt_logs.csv and .json)

# Sample Logs
The app logs for each query:

Timestamp

Model used

Prompt

Partial response

Latency (ms)

Estimated token count

Example CSV row:

timestamp, prompt, model, response, latency_ms, token_count

2025-07-16 12:00:00,"What is AI?","llama-3.1-8b-instant","AI stands for...",142.5,42


# Dependencies
Key packages:

streamlit - Web interface

langchain, langchain_groq, langchain_community - LLM interfacing

python-dotenv - API key management

csv, json, datetime - Logging

Full list in requirements.txt
