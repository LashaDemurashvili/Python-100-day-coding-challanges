import requests
from datetime import datetime


MY_LAT = 41.715137
MY_LONG = 44.827095

# latitude and longitude of Tbilisi
parameters = {
    "lat": MY_LAT,
    "long": MY_LONG,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
# check if there is any error
response.raise_for_status()
data = response.json()

print("sunrise")
sunrise = data['results']['sunrise']
sunrise = sunrise.split("T")[1]
# sunrise = sunrise.split("T")[1].split(":")[0]   # only hour
print(sunrise)

print("\n")
print("sunset")
sunset = data['results']['sunset']
sunset = sunset.split("T")[1]
print(sunset)


now = datetime.now()
print(now)