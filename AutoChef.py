import requests, json
import jwt
from my_recipes import cipher_recipe
from termcolor import colored
#'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', and 'white'

# author: Max Ahartz
# inpired by: hash cracking contest @f0xhunt
# created: Feb 11, 2023
# description: a tool that automates cyberchef

input_value = input("Enter your encrypted message: ")

try:
    decoded_jwt = jwt.decode(input_value, algorithms=['HS256'], verify=False)
    print(colored("\nDecoded JWT:" + str(decoded_jwt), "green"))
    exit()
except Exception as e:
    print(e)
    

###LETS DO MAGIC!!######
url = "http://localhost:3000/magic"
headers = {"Content-Type": "application/json"}


#TEST CASES
#input_value = "JZLU26K2IRJGQWTKIU2U2V2FPJHGURLZLJDUM22ZKRNG2TT2KV4E6R2JO5GWUTTLLFWU2522IRVTGWTNKV4FS3KZGVHFOVTJJYZEK6CZNJCXQT2HJJVE2R2JO5HGUSTLJVCEM2SOGJLGUTSHLEZU6RCSNBGTERJTLJKGY3KNIRSGUWKXLJWE23KVGJGUOUTLLEZE252OKRATETKUKZVFUV2ONJHFOUJTJ5LVKM2OK5ETGTTHHU6Q===="
#input_value = "WUagwsiae6mP8gNtCCLUFpCpCB26RmBDoDD8PacdAmzAzBVjkK2QstFXaKhpC6iUS7RHqXrJtFisoRSgoJ4whjm1arm864qaNq4RcfUmLHrcsAaZc5TXCYifNdgS83gDeejGX46gaiMyuBV6EskHt1scgJ88x2tNSotQDwbGY1mmCob2ARGFvCKYNqiN9ipMq1ZU1mgkdbNuGcb76aRtYWhCGUc8g93UJudhb8htsheZnwTpgqhx83SVJSZXMXUjJT2zmpC7uXWtumqokbdSi88YtkWDAc1Toouh2oH4D4ddmNKJWUDpMwmngUmK14xwmomccPQE9hM172APnSqwxdKQ172RkcAsysnmj5gGtRmVNNh2s359wr6mS2QRP"
#input_value = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.he0ErCNloe4J7Id0Ry2SEDg09lKkZkfsRiGsdX_vgEg"

data = {"input": input_value, "arg": {"depth": 1}}

response = requests.post(url, headers=headers, data=json.dumps(data))

if response.status_code == 200:
    result = response.json()  # dictionary
    print(result)
    exit
    # grab magic steps
    magic_recipe = [matching_op for matching_op in result["value"][0]["recipe"]]
    magic_recipe = str([d["op"] for d in magic_recipe])  # grabs just the names
    magic_recipe = magic_recipe.replace("['", "").replace("']", "").replace("'", "")

    # create a string, iterate thru result dict on value-->"recipe"
    matching_ops = str([matching_op for matching_op in result["value"][0]["recipe"]])

    print(matching_ops, "\n")
    matching_ops = (
        matching_ops.replace("'", '"')
        .replace("False", '"false"')
        .replace("True", '"true"')
    )
    matching_ops = matching_ops[
        :-1
    ]  # clipped last ] at end of string, to join with cipher recipe later (json syntax)
    

else:
    print("Request failed")

candidates = []
###LETS BAKE!!!!####
for recipe in cipher_recipe:
    print(recipe)
    ready_to_bake = matching_ops + "," + recipe + "]"
    print(ready_to_bake)
    url = "http://localhost:3000/bake"
    try:
        data = {"input": input_value, "recipe": json.loads(ready_to_bake)}  # dictionary
        print(data)
        response = requests.post(url, headers=headers, json=data)
        print(response.text)  # string
        if "string" in response.text or "iat" in response.text:
            prettified_recipe = (
                recipe.split(":")[1].replace('"', "").replace("args", "").replace(",", "")
            )
            candidates.extend([prettified_recipe, response.text])
    except Exception as e:
        continue    
print(
    colored(
        """
╭━━━╮╱╱╭╮╱╱╱╭━━━┳╮╱╱╱╱╱╭━╮
┃╭━╮┃╱╭╯╰╮╱╱┃╭━╮┃┃╱╱╱╱╱┃╭╯
┃┃╱┃┣╮┣╮╭╋━━┫┃╱╰┫╰━┳━━┳╯╰╮
┃╰━╯┃┃┃┃┃┃╭╮┃┃╱╭┫╭╮┃┃━╋╮╭╯
┃╭━╮┃╰╯┃╰┫╰╯┃╰━╯┃┃┃┃┃━┫┃┃
╰╯╱╰┻━━┻━┻━━┻━━━┻╯╰┻━━╯╰╯""",
        "green",
    ),
    "\n\n",
)
print(
    colored("\n\n\n******************LIKELY SUSPECTS ARE*******************\n", "cyan")
)

if magic_recipe == "[]":
    print("Sorry, I don't know this one, yet. Good luck!")
else:    
    print(
    "\033[38;5;83mMagic Function is:", magic_recipe.replace(",", " -->"), " \033[0m\n"
)  # print("\033[38;5;83m neon green text \033[0m") #ascii version
for i in range(0, len(candidates) - 1, 2):
    print(colored(candidates[i], "green"))
    print(colored(candidates[i + 1], "blue"), "\n")
    # print(magic_recipe.replace(","," -->"), "-->",i[1], '\n')
