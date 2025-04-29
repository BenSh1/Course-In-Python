
# import csv
import pandas   

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []

#     for row in data :
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
        

#     print(temperatures)





# data = pandas.read_csv("weather_data.csv")

# print(data["temp"])
# print(data["day"])
# print(data["condition"])

# temp_list = data["temp"].to_list()

# average = sum(temp_list) / len(temp_list)
# print("first way to get the average: " ,average)

# print("seconde way to get the average : ",data["temp"].mean())


# print(data["temp"].max())

# print("------------------------------------")
# print(data["condition"])
# print(data.condition)
# print("------------------------------------")


# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# monday_temp_F = monday_temp * 9/5 + 32
# print("temp in fahrenheit : " ,monday_temp_F)
#--------------------------------------------------

# data_dict = {
#     "students": ["Amy" , "James" , "Angela"],
#     "scores" : [76 , 56,65]
# }

# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

#--------------------------------------------------

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

grey_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])

print(grey_squirrel_count)
print(red_squirrel_count)
print(black_squirrel_count)

data_dict = {
     "Fur Color": ["Grey" , "Cinnamon" , "Black"],
     "Count" : [grey_squirrel_count , red_squirrel_count,black_squirrel_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
