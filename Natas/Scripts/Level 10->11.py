import base64

plaintext = b'{"showpassword":"no","bgcolor":"#ffffff"}'

cookie = "EGAgHwQ1IxYYMSQYGSZxTUksPFVHYDEQCC0/GBlgaVVIJDURDSQ1VRY="

ciphertext = base64.b64decode(cookie)

key = b''

for i in range(len(ciphertext)):
    key += bytes([ciphertext[i] ^ plaintext[i]])

print(key)
