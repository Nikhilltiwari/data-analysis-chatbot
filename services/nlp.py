import requests

LLAMA_API_URL = "http://localhost:5000/llama"

def call_llama_model(prompt: str, context: dict):
    response = requests.post(LLAMA_API_URL, json={'prompt': prompt, 'context': context})
    return response.json().get('response')

