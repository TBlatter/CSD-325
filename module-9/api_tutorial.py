#tyson blatter 9.1 4-25
import requests



url = 'http://api.open-notify.org/astros.json'
response = requests.get(url)

print("Status Code:", response.status_code)
print("\nOutput:")
data = response.json()
print(f"There are {data['number']} people in space right now:\n")
for person in data['people']:
    print(f"- {person['name']} on {person['craft']}")
