#tyson blatter 9.1 4-25

import requests

url = "https://catfact.ninja/fact"

# Step 1: Test the connection
response = requests.get(url)
print("Connection Test - Status Code:", response.status_code)

# Step 2: Raw response it will not look as clean
print("\nRaw Response Text:")
print(response.text)

# Step 3: Formatted output - cleaner outlook
data = response.json()

print("\nFormatted Cat Fact:")
print(f"Fact: {data['fact']}")
print(f"Length: {data['length']}")
