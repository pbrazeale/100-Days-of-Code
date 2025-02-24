# import csv

# # with open("weather_data.csv") as weather_data:
# #     data = weather_data.readlines()

# with open("weather_data.csv") as weather_data:
#     data = csv.reader(weather_data)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#         print(temperatures)

# Pandas doc https://pandas.pydata.org/docs/
import pandas

data = pandas.read_csv("weather_data.csv")

print(data["temp"])
