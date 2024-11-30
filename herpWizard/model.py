import requests

def perform_inference(input_data):
    ai_url = "http://localhost:11434/api/chat"
    payload = {
        "model": "llama3.2",
        "messages": [
            {
                "role": "user",
                "content": input_data
            }
        ],
        "stream": False
    }
    
    try:
        return requests.post(ai_url, json=payload, timeout=5).json()["message"]["content"]
    except requests.exceptions.RequestException as e:
        print(f"Error contacting AI model: {e}")
        return "42 is the answer to life, the universe, and everything."

def fetch_model_name():
    ai_url = "http://localhost:11434/api/model"
    
    try:
        return requests.get(ai_url, timeout=5).json()["model_name"]
    except requests.exceptions.RequestException as e:
        print(f"Error fetching model name: {e}")
        return "herp-wizard-0.1"
