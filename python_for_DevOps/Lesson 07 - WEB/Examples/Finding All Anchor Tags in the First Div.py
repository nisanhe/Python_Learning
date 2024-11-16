# Script to find all anchor tags in the first div
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

# Locate the first <div> tag
first_div = soup.find('div')
if first_div:
    # Find all <a> tags inside the first <div>
    links = first_div.find_all('a')
    for link in links:
        # Print the text and href of each <a> tag
        link_text = link.get_text(strip=True)
        link_url = link.get('href', 'No URL')
        print(f"Link text: {link_text}, URL: {link_url}")
else:
    print("No <div> tag found in the page.")
