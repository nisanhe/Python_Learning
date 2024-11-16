# Using session to maintain authentication
import requests

# Start a session
session = requests.Session()

# Login to the site
login_url = "http://example.com/login"
credentials = {"username": "user", "password": "pass"}
session.post(login_url, data=credentials)

# Access a protected page
protected_url = "http://example.com/protected"
response = session.get(protected_url)
print(response.text)
