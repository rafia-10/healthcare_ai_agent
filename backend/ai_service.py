import requests
import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def call_gemini(user_input):
    url = "https://api.ai.google/v1/gemini:processText"
    headers = {
        "Authorization": f"Bearer {GEMINI_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "input": user_input
    }
    response = requests.post(url, json=payload, headers=headers)
    data = response.json()
    
    # Example: parse response to get intent, entities, confidence
    intent = data["intent"]
    entities = data.get("entities", {})
    confidence = data.get("confidence", 1.0)
    
    return intent, entities, confidence
