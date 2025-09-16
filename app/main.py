#Import FastAPI for creating the backend and BaseModel for request validation
from fastapi import FastAPI
from pydantic import BaseModel

# Initialize FastAPI app
app = FastAPI()

# Pydantic model to define the expected input for the summarizer
class TextInput(BaseModel):
    text: str # The text the user wants to summarize

# Root endpoint to test if the API is running
@app.get("/")
def read_root():
    return {"message": "Hello, world!"}

# Endpoint to summarize text
@app.post("/summarize")
def summarize(input: TextInput):
    """
    Accepts a POST request with JSON containing 'text'.
    Returns a dummy summary (first 100 characters or full text if shorter).
    """
    # Truncate text to 100 characters as a placeholder summarization
    summary = input.text[:100] + "..." if len(input.text) > 100 else input.text
    # Return the summary as JSON
    return {"summary": summary}
