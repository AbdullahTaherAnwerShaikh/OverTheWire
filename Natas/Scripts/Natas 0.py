import requests
import re #regular expressions

username = "natas0"
password = "natas0"

url = 'http://%s.natas.labs.overthewire.org/' % username

response = requests.get(url, auth=(username, password))
content = response.text

print (re.findall("<!--The password for natas1 is (.*) -->",content)[0])
