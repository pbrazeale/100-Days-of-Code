# # import csv

# # # with open("weather_data.csv") as weather_data:
# # #     data = weather_data.readlines()

# # with open("weather_data.csv") as weather_data:
# #     data = csv.reader(weather_data)
# #     temperatures = []
# #     for row in data:
# #         if row[1] != "temp":
# #             temperatures.append(int(row[1]))
# #         print(temperatures)

# # Pandas doc https://pandas.pydata.org/docs/
# import pandas

# # data = pandas.read_csv("weather_data.csv")

# # print(type(data))

# # print(data["temp"])

# # data_dict = data.to_dict()
# # print(data_dict)

# # temp_list = data["temp"].to_list()
# # print(temp_list)

# # avg_temp = data["temp"].mean()
# # max_temp = data.temp.max()

# # print(max_temp)

# # print(data[data.day == "Monday"])
# # print(data[data.temp == max_temp])

# # monday = data[data.day == "Monday"]
# # temp_to_f = monday.temp[0] * (9 / 5) + 32
# # print(temp_to_f)

# # Create a dataframe from scratch
# data_dict = {"students": ["Amy", "James", "Angela"], "scores": [76, 56, 65]}
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")

import csv
import pandas

# idneitfy number of Gray, Cinnamon, Black squirrels
data = pandas.read_csv("2018_Central_Park_Squirrel_Census.csv")
# gray
gray = data[data["Primary Fur Color"] == "Gray"]
gray_count = len(gray)
print(gray_count)
cinnamon = data[data["Primary Fur Color"] == "Cinnamon"]
cinnamon_count = len(cinnamon)

black = data[data["Primary Fur Color"] == "Black"]
black_count = len(black)

# Build new CSV
# Fur Color, Count
processed_primary_colors = {
    "Fur Color": ["gray", "cinnamon", "balck"],
    "Count": [gray_count, cinnamon_count, black_count],
}
squirrel_count = pandas.DataFrame(processed_primary_colors)
print(squirrel_count)
squirrel_count.to_csv("primary_color_squrrel_count.csv")
