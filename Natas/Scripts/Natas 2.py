import requests
import re #regular expressions

username = "natas1"
password = "scfWG6qNEIdzqVyfRwEGXyNUfFZkZeQ7"

url = 'http://%s.natas.labs.overthewire.org/' % username

response = requests.get(url, auth=(username, password))
content = response.text

print (re.findall("<!--The password for natas2 is (.*) -->",content)[0])
