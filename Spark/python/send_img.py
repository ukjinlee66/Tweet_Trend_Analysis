import base64
import json

import requests

api = 'http://192.168.0.10:8080/img'
image_file = 'wordword.png'

with open(image_file, "rb") as f:
    im_bytes = f.read()
im_b64 = base64.b64encode(im_bytes).decode("utf-8")

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

payload = json.dumps({"img": im_b64})
print('json dump')
print(payload)
response = requests.post(api, data=payload, headers=headers)
try:
    data = response.json()
    print(data)
except requests.exceptions.RequestException:
    print(response.text)
