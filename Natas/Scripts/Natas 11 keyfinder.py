import base64

plaintext = b'{"showpassword":"no","bgcolor":"#ffffff"}'
cookie = "EGAgHwQ1IxYYMSQYGSZxTUksPFVHYDEQCC0/GBlgaVVIJDURDSQ1VRY="
ciphertext = base64.b64decode(cookie)

def xor_encrypt(input,key):
    finalkey = b''

    for i in range(len(input)):
        finalkey += bytes([key[i] ^ input[i % len(input)]])

    print(finalkey)

xor_encrypt(plaintext,ciphertext)
