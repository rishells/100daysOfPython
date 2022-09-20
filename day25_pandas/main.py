import csv
import pandas as pd
# with open('day25_pandas/weather_data.csv') as file:
#     print(file.readlines())


# with open('day25_pandas/weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
# print(temperatures)

# data = pd.read_csv('weather_data.csv')
# # data_dict = data.to_dict()
# #print(data_dict)
# data['Validations'] = data.apply(lambda x: x.condition in x.full_condition, axis = 1)
# print(data)

# temp_list = data["temp"].to_list()
# total_temp = 0
# for temp in temp_list:
#         total_temp += temp
# average_temp = total_temp / len(temp_list)
# print(total_temp)
# print(len(temp_list))
# print(round(average_temp,2))

# #Computation in Columns
# print(data["temp"].mean())
# print(data["temp"].max())

# #Get Data in Columns
# print(data.condition)
# print(data["condition"])

#Get Data in Row
# print(data[data.day == "Monday"])
# print(data[data.temp == max(data.temp)])
# print(data[data.temp == data.temp.max()])


# def celsius_to_fahrenheit(temp):
#     return (temp * 1.8) +32
# monday = data[data.day == "Monday"]

# print(celsius_to_fahrenheit(monday.temp))


# Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }

# data = pd.DataFrame(data_dict)

# data.to_csv("new_data.csv")


#Squirel own solution
# data = pd.read_csv('/home/rishells/rcdev/100daysOfPython/day25_pandas/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
# #print(data["Primary Fur Color"].drop_duplicates())

# data_csv = data["Primary Fur Color"].value_counts()

# #data_csv = pd.DataFrame(data)
# data_csv.to_csv("/home/rishells/rcdev/100daysOfPython/day25_pandas/squirrel_count.csv")


#Squirel course solution
data = pd.read_csv('/home/rishells/rcdev/100daysOfPython/day25_pandas/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(gray_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color" : ["Gray", "Cinnamon", "Black"],
    "Count" : [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pd.DataFrame(data_dict)
df.to_csv("/home/rishells/rcdev/100daysOfPython/day25_pandas/squirrel_count2.csv")
