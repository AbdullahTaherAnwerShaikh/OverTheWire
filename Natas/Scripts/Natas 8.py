import requests
import re #regular expressions

username = "natas8"
password = "ugXL95KQmUAJJj6bMezOlBNDyI9Imwkc"

url = 'http://%s.natas.labs.overthewire.org' % username

foundSecret = "oubWYf2kBq"
data={"secret":foundSecret,"submit":"submit"}

session = requests.Session() #Maintains a session
#response = session.get(url , auth=(username, password))
response = session.post(url , auth=(username, password), data=data)
content = response.text

#print (content)
print (re.findall("natas9 is (.*)",content)[0])
