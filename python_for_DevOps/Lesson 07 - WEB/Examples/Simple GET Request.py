# Using urllib3 to make a GET request
import urllib3

# Create a PoolManager instance
http = urllib3.PoolManager()

# Send a GET request
url = "http://example.com"
response = http.request('GET', url)

# Print the response data
print(response.data.decode('utf-8'))
