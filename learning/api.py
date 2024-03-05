import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print (response.status_code)
print (response.content)

response.raise_for_status()