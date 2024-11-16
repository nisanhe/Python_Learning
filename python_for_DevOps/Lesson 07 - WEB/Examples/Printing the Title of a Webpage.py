# Script to fetch and print the title of a webpage
from bs4 import BeautifulSoup
import requests

# Ask the user for a URL
url = input("Enter the URL of the website: ")

# Ensure the URL includes HTTP/HTTPS
if not url.startswith("http://") and not url.startswith("https://"):
    url = "http://" + url

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Extract and print the title tag
title = soup.title.string if soup.title else "No title found"
print(f"The title of the page is: {title}")
