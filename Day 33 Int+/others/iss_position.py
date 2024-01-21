import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")

data = response.json()["iss_position"]

latitude = response.json()["iss_position"]["latitude"]
longitude = response.json()["iss_position"]["longitude"]

iss_position = (latitude, longitude)
print(iss_position)

