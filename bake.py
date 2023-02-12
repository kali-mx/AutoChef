import requests,json,re

#####Use MAGIC!!!#####

Chall_hash = "JZLU26K2IRJGQWTKIU2U2V2FPJHGURLZLJDUM22ZKRNG2TT2KV4E6R2JO5GWUTTLLFWU2522IRVTGWTNKV4FS3KZGVHFOVTJJYZEK6CZNJCXQT2HJJVE2R2JO5HGUSTLJVCEM2SOGJLGUTSHLEZU6RCSNBGTERJTLJKGY3KNIRSGUWKXLJWE23KVGJGUOUTLLEZE252OKRATETKUKZVFUV2ONJHFOUJTJ5LVKM2OK5ETGTTHHU6Q===="
url = "http://localhost:3000/magic"

headers = {
    "accept": "application/json",
    "Content-Type": "application/json"
}

payload = {
    "input": Chall_hash,
    "args": {
        "depth": 1
    }
}



#dumps converts json to a string
response = requests.post(url, headers=headers, data=json.dumps(payload))

if response.status_code == 200:
    print(type(response))
    text = response.text
    #print(text)
    
    match = re.search(r'"matchingOps"', text)
    #match = re.search("matchingOps", text)
    print("Found match:", match.group(0))
    
    #ops = [op["op"] for op in matching_ops]
    #print(" ".join(ops))
else:
    print("Request failed with status code:", response.status_code)



###Lets BAKE!!!####
url = "http://localhost:3000/bake"

headers = {
    "Content-Type": "application/json"
}

payload = {
    "input": Chall_hash,
    "recipe": [
        {
            "op": "From Base32",
            "args": ["A-Z2-7=", True]
        },
        {
            "op": "From Base64",
            "args": ["A-Za-z0-9+/=", True, False]
        }
    ]
}

response = requests.post(url, headers=headers, json=payload)

print(response.status_code)
print(response.json())
data = response.json()
byte_array = bytes(data["value"])
string = byte_array.decode('utf-8')
print(string)


payload = {"input": string, "recipe": [{"op":"A1Z26 Cipher Decode","args":["Space"]},{"op":"RC2 Decrypt","args":[{"option":"Hex","string":""},{"option":"Hex","string":""},"Hex","Raw"]}]}

response = requests.post(url, headers=headers, json=payload)
print(response.text)
print(response.status_code)
print(response.json())
data = response.json()
string = byte_array.decode('utf-8')
byte_array = bytes(data["value"])

print(string)


