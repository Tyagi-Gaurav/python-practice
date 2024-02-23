import pandas

# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data["temp"])
#
# dict = data.to_dict()
# print(dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# # Get Data in columns
# print(round(sum(temp_list) / len(temp_list), 2))
# print(data["temp"].mean())
# print(data["temp"].max())
# print(data.temp.max())
#
# # Get Data in row using conditions
# print(data[data.day == "Monday"])
# print(data.iloc[data["temp"].idxmax()])
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# print(monday.temp[0])
#
# # Create a dataframe from scratch
# custom_data_dict = {
#     "students": ["Amy", "James", "Ans"],
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(custom_data_dict)
# data.to_csv()

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240222.csv")
print (data.groupby("Primary Fur Color").count())

grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fun Color" : ["Gray", "Cinnamon", "Black"],
    "Count" : [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")