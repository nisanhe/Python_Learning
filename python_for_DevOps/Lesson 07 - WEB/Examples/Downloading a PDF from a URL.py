# Script to download a PDF file from a URL
import requests

# Specify the PDF URL
pdf_url = "http://example.com/sample.pdf"

# Specify the local filename to save as
local_filename = "Hack-U-Self.pdf"

# Send a GET request to fetch the PDF content
response = requests.get(pdf_url)

# Write the content to a local file
with open(local_filename, "wb") as file:
    file.write(response.content)

print(f"PDF downloaded and saved as {local_filename}")
