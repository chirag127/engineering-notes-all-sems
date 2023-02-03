import requests

import json
import tiktoken

ENCODER = tiktoken.get_encoding("gpt2")


def get_max_tokens(prompt: str) -> int:
    """
    Get the max tokens for a prompt
    """
    return 3500 - len(ENCODER.encode(prompt))

def pawan(p,api):

    response = requests.post('https://chatgpt.pawan.krd/init', headers={
        'Content-Type': 'application/json'
    }, data=json.dumps({
        'key': '***REMOVED***',
        'options':{
  "temperature": 0.2,
  "max_tokens": get_max_tokens(p),
  "top_p": 0.9,
  "frequency_penalty": 0,
  "presence_penalty": 0,
  "instructions": '''You are an AI language model developed by OpenAI, called ChatGPT. you have been trained on a large corpus of text data to generate human-like text and answer questions. You can answer comprehensively.''',
  "stop": "<|im_end|>"
}

    }))

    if response.json()


    response = requests.post('https://chatgpt.pawan.krd/ask', headers={
        'Content-Type': 'application/json'
    }, data=json.dumps({
        'key': '***REMOVED***',
        'prompt': 'who are you?',
        'id': 'default'
    }))

    if response.json()