# Sending custom headers in an HTTP request
import requests

url = "http://example.com"
headers = {
    "User-Agent": "MyApp/1.0",
    "Authorization": "Bearer my-token"
}

response = requests.get(url, headers=headers)
print(response.text)
