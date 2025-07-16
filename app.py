import streamlit as st
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
from langchain_groq import ChatGroq
import os
import time
import json
import csv
from datetime import datetime
from dotenv import load_dotenv

# Loading environment variables
load_dotenv()
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
groq_api_key = os.getenv("GROQ_API_KEY")

# Ensuring logs directory exists
os.makedirs("logs", exist_ok=True)

# Prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "Act as a helpful assistant. Your job is to provide informative and relevant answers to user queries."),
        ("user", "Question:{question}")
    ]
)

def generate_response(question, llm_name):
    llm = ChatGroq(model=llm_name, api_key=groq_api_key)
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    start_time = time.time()
    answer = chain.invoke({'question': question})
    latency_ms = round((time.time() - start_time) * 1000, 2)

    # Estimate token count (naive approx: 1 token ≈ 4 chars)
    token_count = (len(question) + len(answer)) // 4

    return {
        "response": answer,
        "latency_ms": latency_ms,
        "token_count": token_count
    }

def log_response(question, model_name, result):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    row = {
        "timestamp": timestamp,
        "prompt": question,
        "model": model_name,
        "response": result["response"][:100],  # Truncate response for logging
        "latency_ms": result["latency_ms"],
        "token_count": result["token_count"]
    }

    # Log to CSV
    csv_file = "logs/prompt_logs.csv"
    write_header = not os.path.exists(csv_file)
    with open(csv_file, "a", newline="") as cf:
        writer = csv.DictWriter(cf, fieldnames=row.keys())
        if write_header:
            writer.writeheader()
        writer.writerow(row)

    # Log to JSON
    with open("logs/prompt_logs.json", "a") as jf:
        json.dump(row, jf)
        jf.write("\n")

# Streamlit UI
st.title("Multi-Model LLM Prompt Service")

st.sidebar.header("Model Configuration")
llm = st.sidebar.selectbox("Select Open Source Model", ["gemma2-9b-it", "llama-3.1-8b-instant"])

st.markdown(f"Hello! I'm {llm}. Ask me anything")
user_input = st.text_input("You:")

if user_input:
    result = generate_response(user_input, llm)

    # JSON response display
    st.subheader("Response (JSON Format)")
    st.json(result)

    # Log the response
    log_response(user_input, llm, result)
else:
    st.info("Please enter a question.")
