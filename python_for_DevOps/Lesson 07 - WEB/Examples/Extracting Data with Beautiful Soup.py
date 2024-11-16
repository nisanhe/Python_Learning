# Extracting data using BeautifulSoup
from bs4 import BeautifulSoup
import requests

url = "http://example.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract all links
links = soup.find_all('a')
for link in links:
    print(link.get('href'))
