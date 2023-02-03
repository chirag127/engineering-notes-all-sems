nalty": 0,
            "instructions": '''You are an AI language model developed by OpenAI, called ChatGPT. you have been trained on a large corpus of text data to generate human-like text and answer questions. You can answer comprehensively.''',
            "stop": "<|im_end|>"
        }

    }))

    return response.json()["response"]

if __name__ == '__main__':
    print(pawan("hello", "***REMOVED***"))
