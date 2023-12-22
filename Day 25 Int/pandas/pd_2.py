import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray = len(data[data['Primary Fur Color'] == 'Gray'])
red = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black = len(data[data['Primary Fur Color'] == 'Black'])

data_dict = {
    "Fur colors": ["Gray", "black", "Red"],
    "Count": [gray, black, red]
}

# export as csv file
data = pandas.DataFrame(data_dict)
data.to_csv('FurColor.csv')
