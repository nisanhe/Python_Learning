# Demonstrating GET and POST requests with the requests library
import requests

# GET request
get_response = requests.get("http://example.com", params={"key": "value"})
print("GET Response:", get_response.text)

# POST request
post_response = requests.post("http://example.com", data={"key": "value"})
print("POST Response:", post_response.text)
