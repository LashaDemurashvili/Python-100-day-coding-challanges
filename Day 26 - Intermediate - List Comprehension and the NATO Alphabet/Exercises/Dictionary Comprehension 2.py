# (temp_c * 9/5) + 32 = temp_f
# convert all C temperature to F

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {weekday: temp_c * 9 / 5 + 32 for (weekday, temp_c) in weather_c.items()}

print(weather_f)
