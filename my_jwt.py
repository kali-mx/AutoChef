import requests
import json

url = "http://127.0.0.1:3000/bake"

headers = {
    "accept": "application/json",
    "Content-Type": "application/json"
}

data = {
    "input": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.he0ErCNloe4J7Id0Ry2SEDg09lKkZkfsRiGsdX_vgEg",
    "recipe": [ {"op": "JWT Decode", "args": []} ] }

#serialize an object to a JSON-formatted string using dumps()
response = requests.post(url, headers=headers, data=json.dumps(data))

if response.status_code == 200:
    result = response.json()
    print(json.dumps(result, indent=4))
else:
    print("Request failed with status code:", response.status_code)
