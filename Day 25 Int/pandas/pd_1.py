# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)


# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)
#

import pandas

data = pandas.read_csv("weather_data.csv")

data_dict = data.to_dict()
print(data_dict)

data_list = data['temp'].to_list()

# mean
average_temp = sum(data_list) / len(data_list)
print(round(average_temp, 1))

# max
print(data['temp'].max())

# get data in columns
# this two method is the same
print(data['temp'])
print(data.temp)

# get date in row
mx = data['temp'].max()
print(data[data.temp == mx])

# temperature in F
monday = data[data.day == "Monday"]
monday_temp_f = monday.temp * 9 / 5 + 32
print(monday_temp_f)


# create dataframe from scratch
my_dict = {
    "name": ["lasha", "gio", "beka"],
    "surname": ["demurashvili", "sabadze", "giorgobiani"]
}

# save file different format
data = pandas.DataFrame(my_dict)
data.to_csv("students.csv")

