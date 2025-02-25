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

# data = pandas.read_csv("weather_data.csv")

# print(type(data))

# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)

# avg_temp = data["temp"].mean()
# max_temp = data.temp.max()

# print(max_temp)

# print(data[data.day == "Monday"])
# print(data[data.temp == max_temp])

# monday = data[data.day == "Monday"]
# temp_to_f = monday.temp[0] * (9 / 5) + 32
# print(temp_to_f)

# Create a dataframe from scratch
data_dict = {"students": ["Amy", "James", "Angela"], "scores": [76, 56, 65]}
data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")
