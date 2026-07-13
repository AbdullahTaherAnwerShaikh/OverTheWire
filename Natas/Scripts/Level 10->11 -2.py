import base64

plaintext = b'{"showpassword":"yes","bgcolor":"#ffffff"}'
key = b'kBSw'
outtext = b''
for i in range(len(plaintext)):
    outtext += bytes([plaintext[i] ^ key[i % len(key)]])

print(base64.b64encode(outtext).decode())
