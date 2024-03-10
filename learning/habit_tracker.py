import requests
from datetime import datetime as dt

url = "https://pixe.la/v1/users"
USERNAME = "chonku"
TOKEN = "n$&59*s&gq2o"
GRAPHID = "graph1"

body = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# Create User
# curl -X POST https://pixe.la/v1/users -d '{"token":"thisissecret", "username":"a-know", "":"yes", "notMinor":"yes"}'

# Create Graph
# curl -X POST https://pixe.la/v1/users/a-know/graphs -H 'X-USER-TOKEN:thisissecret' -d '{"id":"test-graph","name":"graph-name","unit":"commit","type":"int","color":"shibafu"}'
graph_endpoint = f"{url}/{USERNAME}/graphs/{GRAPHID}"
graph_config = {
    "id": GRAPHID,
    "name": "some-graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

time = dt.now().strftime("%Y%m%d")

pixel_data = {
    "date": time,
    "quantity": "9.83"
}

response = requests.post(graph_endpoint, json=pixel_data, headers=headers)

print(response.json())
