import requests

# original data
# {"message": "success", "iss_position": {"latitude": "-45.8627", "longitude": "-120.1955"}, "timestamp": 1705860189}


response = requests.get(url="http://api.open-notify.org/iss-now.json")

data = response.json()["iss_position"]

latitude = response.json()["iss_position"]["latitude"]
longitude = response.json()["iss_position"]["longitude"]

iss_position = (latitude, longitude)
print(iss_position)

