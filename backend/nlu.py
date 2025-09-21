import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def call_groq(user_input):
    url = "https://api.groq.com/openai/v1/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama-3.1-8b-instant",
        "messages": [
            {
                "role": "system",
                "content": """You are an AI that extracts structured data from user input.
Always respond with ONLY valid JSON. 
Schema:
{
  "intent": "book_appointment" | "reschedule_appointment" | "cancel_appointment" | "faq" | "unknown",
  "entities": {
      "patient_name": "string or null",
      "doctor": "string or null",
      "datetime": "string or null",
      "email": "string or null"
  },
  "confidence": float
}"""
            },
            {"role": "user", "content": user_input}
        ],
        "temperature": 0
    }

    response = requests.post(url, headers=headers, json=payload)
    data = response.json()

    try:
        message = data["choices"][0]["message"]["content"]
        parsed = json.loads(message)
        return (
            parsed.get("intent"),
            parsed.get("entities"),
            parsed.get("confidence")
        )
    except Exception as e:
        print("Error parsing response:", e, data)
        print("Raw response:", response.text)
        return None
