**AI Text Summarizer**

A simple FastAPI app that summarizes text using OpenAI's GPT-3.5-turbo.
This project demonstrates a working API, a Python-based frontend using Streamlit, automated tests, and a CI workflow.

**Features**

- /summarize endpoint to generate AI-powered summaries of any text

- Streamlit frontend for interactive use

- Automated tests using mocked OpenAI responses (runs without an API key)

- Continuous Integration with GitHub Actions

- Clean project structure and easy setup

Setup & Run

**1. Clone the repository**

```
git clone https://github.com/yourusername/ai-summarizer.git
cd ai-summarizer
``````


**2. Create a virtual environment (optional but recommended)**
``````
python -m venv venv

# Git Bash / Linux:
source venv/Scripts/activate

# PowerShell:
.\venv\Scripts\activate
``````


**3. Install dependencies**
``````
pip install -r requirements.txt
``````

**4. Set your OpenAI API key (optional for real summaries)**
``````
# Linux / Git Bash
export OPENAI_API_KEY="sk-xxx"

# Windows PowerShell
setx OPENAI_API_KEY "sk-xxx"
``````

Note: Tests run without an API key thanks to mocking.

**5. Run the FastAPI app**
``````
uvicorn app.main:app --reload
``````
**6 Run the Streamlit frontend (in a separate terminal)***
```
streamlit run app/frontend.py
```

**7 Use the app**
- Type text in the Streamlit app and click **Summarize**
- Or test the API directly
``````
curl -X POST "http://127.0.0.1:8000/summarize" \
     -H "Content-Type: application/json" \
     -d '{"text":"FastAPI is a modern Python web framework."}'
``````
**Testing**

Run all tests with:
``````
pytest -v
``````

- Mocked tests ensure that you don’t need an OpenAI API key.
- Confirms both the root endpoint and /summarize work as expected.

**Project Structure**
```text
ai-summarizer/
├─ app/
│  ├─ main.py          # FastAPI app with /summarize endpoint
├─ tests/
│  ├─ test_app.py      # Mocked tests for API endpoints
├─ .github/workflows/
│  ├─ ci.yml           # GitHub Actions workflow for CI
├─ requirements.txt
├─ README.md
├─ .gitignore
``````

**Notes**

- All tests and CI are fully functional without an OpenAI API key.

- For production use, ensure your OPENAI_API_KEY is stored securely (environment variables or secret management).

**License**

MIT License