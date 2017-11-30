import requests
import json

url = 'http://210.51.169.193:8080/login.whtml'

jsonData = json.dumps(
    {
        "user": {
            "userName": "60000852",
            "password": "60000852"
        },
        "loginURL": "http://210.51.169.193:8080/login.html"
    })
response = requests.post(url, data=jsonData, headers={'content-type': 'application/json'})
s = json.loads(response.text)
print(s.keys)
