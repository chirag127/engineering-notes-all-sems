# Web Technology
```python
# This is an example of a simple Python program that uses web technology to make a GET request to an API and print the response.

import requests

url = 'https://api.example.com/data'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print('An error occurred:', response.status_code)
```