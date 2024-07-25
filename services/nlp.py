import requests
from prompt import get_llm_prompt

def analyze_query_with_llm(query: str, df_columns: list):
    llm_prompt = get_llm_prompt()
    response = requests.post('OLLAMA_API_URL', json={'prompt': llm_prompt, 'query': query, 'columns': df_columns})
    answer = response.json().get('answer')
    return answer
