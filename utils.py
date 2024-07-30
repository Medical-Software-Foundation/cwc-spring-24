import os
import requests

OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
OPENAI_URL = 'https://api.openai.com/v1/chat/completions'


def query_openai(prompt):
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }
    system_message = {
        "role": "system",
        "content": "You are a seasoned primary care physician"
    }
    user_message = {"role": "user", "content": prompt}
    data = {
        "model": "gpt-4",
        "messages": [system_message, user_message],
        "temperature": 0.0
    }
    resp = requests.post(OPENAI_URL, json=data, headers=headers)
    if resp.status_code != 200:
        raise Exception(f'Error querying OpenAI: {resp.status_code}')

    return resp.json()['choices'][0]['message']['content']
