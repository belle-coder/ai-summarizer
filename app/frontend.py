import streamlit as st
import requests

st.set_page_config(page_title="AI Text Summarizer")

st.title("AI Text Summarizer")
st.write("Enter text below and get a summary using the backend API.")

# Text input from user
user_input = st.text_area("Input Text", "")

# Button to send request
if st.button("Summarize"):
    if user_input.strip() == "":
        st.warning("Please enter some text to summarize.")
    else:
        try:
            # Make POST request to the backend
            response = requests.post(
                "http://127.0.0.1:8000/summarize",
                json={"text": user_input}
            )
            if response.status_code == 200:
                summary = response.json().get("summary", "")
                st.subheader("Summary")
                st.write(summary)
            else:
                st.error(f"Error from API: {response.status_code}")
        except Exception as e:
            st.error(f"Could not reach the API: {e}")
