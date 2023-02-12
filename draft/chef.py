import requests,json

def decode_hash(hash_value, operation_list):
    # URL for CyberChef API
    url = "https://prod.apifor.io/cyberchef/magic"

    headers = {
        'Content-Type': 'application/json',
        'x-api-key': 'GBqMkpelQd3aZYIAJyiJZ15ZfXctbqhc67o7MggJ'
    }

    # Prepare the input data
    input_data = {
        'input': hash_value,
        'recipe': operation_list
    }

    # Make a POST request to the API with input data
    response = requests.post(url, json=input_data, headers=headers)
    print(response)

    try:
        # Extract the decoded output
        decoded_output = response.json()['output']
    except json.decoder.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        print(f"Response status code: {response.status_code}")
        print(f"Response content: {response.content}")
        decoded_output = None

    # Extract the decoded output
    decoded_output = response.json()['output']
    print(decoded_output)
    return decoded_output

# The input hash to be decoded
hash_value = "JZLU26K2IRJGQWTKIU2U2V2FPJHGURLZLJDUM22ZKRNG2TT2KV4E6R2JO5GWUTTLLFWU2522IRVTGWTNKV4FS3KZGVHFOVTJJYZEK6CZNJCXQT2HJJVE2R2JO5HGUSTLJVCEM2SOGJLGUTSHLEZU6RCSNBGTERJTLJKGY3KNIRSGUWKXLJWE23KVGJGUOUTLLEZE252OKRATETKUKZVFUV2ONJHFOUJTJ5LVKM2OK5ETGTTHHU6Q===="

# The list of encoding options to be tried
encoding_options = [
    "From Base64",
    "From Base32"
    # "Base16 (Hex)",
    # "URL Encode",
    # "HTML Encode",
    # "HTML Entities",
    # "Morse Code",
    # "ASCII85",
    # "Z-Base-32",
    # "Base58Check"
]

# Try each encoding option one by one
for option in encoding_options:
    operation_list = [
        {
            "op": option,
            "args": []
        }
    ]
    print(operation_list)
    decoded_output = decode_hash(hash_value, operation_list)

    print(f"{option}: {decoded_output}")

