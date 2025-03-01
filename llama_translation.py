import requests
import os

OLLAMA_API_KEY = os.getenv("OLLAMA_API_KEY")

def llama_translate(text, source_lang, target_lang):
    url = "https://api.ollama.com/translate"
    headers = {"Authorization": f"Bearer {OLLAMA_API_KEY}", "Content-Type": "application/json"}
    payload = {"text": text, "source": source_lang, "target": target_lang}
    
    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 200:
        return response.json().get("translated_text", "Translation failed.")
    return f"Error connecting to Llama API: {response.status_code}"