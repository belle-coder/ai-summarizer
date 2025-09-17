#Import FastAPI for creating the backend and BaseModel for request validation
import os
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from openai import OpenAI

# Load variables from .env
load_dotenv()

# Get the API key
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# Initialize FastAPI app
app = FastAPI()

# Pydantic model to define the expected input for the summarizer
class TextInput(BaseModel):
    text: str # The text the user wants to summarize

# Simple root endpoint to test if the API is running
@app.get("/")
def read_root():
    return {"message": "Hello, world!"}

# Endpoint to summarize text
@app.post("/summarize")
def summarize(input: TextInput):
    """
    Summarize text using OpenAI.
    """
    try:
        # Modern API call
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that summarizes text."},
                {"role": "user", "content": input.text}
            ],
            temperature=0.5,
            max_tokens=150
        )
        summary = response.choices[0].message.content.strip()
    except Exception as e:
        summary = f"Error: {e}"

    return {"summary": summary}
