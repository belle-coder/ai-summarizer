# tests/test_app.py
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from app.main import app
import os
import pytest

client = TestClient(app)

@pytest.mark.skipif(
    os.getenv("CI") == "true",
    reason="Skip root test in CI"
)
def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, world!"}

def test_summarize_mock():
    # Mock OpenAI so no API key is needed
    with patch("app.main.OpenAI") as MockOpenAI:
        mock_client = MockOpenAI.return_value
        mock_client.chat.completions.create.return_value.choices = [
            type("obj", (), {"message": type("msg", (), {"content": "Mocked summary"})()})()
        ]

        response = client.post("/summarize", json={"text": "Test input"})
        assert response.status_code == 200
        body = response.json()
        assert "summary" in body
        assert body["summary"] == "Mocked summary"
