
# csv way
import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for i, row in enumerate(data):
        if i != 0:
            temperatures.append(int(row[1]))
    print(temperatures)

# pandas way
import pandas as pd

data = pd.read_csv("weather_data.csv")
data_list = data.temp.to_list()
print(data_list)
print(data.to_dict())

# average temp
print(data.temp.mean())

# max temp
print(data.temp.max())
print(data[data.temp == data.temp.max()])
