import json
from dotenv import load_dotenv
import os
import requests
import sys

load_dotenv()
input_string = sys.stdin.readline()
while input_string != "\n":
    api_url = 'https://api.openai.com/v1/chat/completions'
    api_key = os.environ.get('API_KEY')

    # Define query parameters
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + api_key,
    }

    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{
            "role": "user",
            "content": input_string,
        }]
    }

    req = requests.post(
        api_url,
        data=json.dumps(data),
        headers=headers,
    )
    answer = json.loads(req.text)["choices"][0]["message"]["content"]
    print(answer)
    input_string = sys.stdin.readline()

