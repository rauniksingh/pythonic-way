import pandas
# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     next(data)  # Skip header row

#     for row in data:
#         print(row)
        
#         temp = int(row[1])
#         temperatures.append(temp)
    
#     print(temperatures)


# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []

#     for row in data:
#         if row[1] != "temp":

#             temp = int(row[1])
#             temperatures.append(temp)
    
#     print(temperatures)

data = pandas.read_csv("weather_data.csv")
# print(data)
# print(type(data))
# print(data['temp'])
# print(type(data['temp']))

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)
# print(len(temp_list))

# temp_avg = data["temp"].mean()
# print(temp_avg)

# temp_avg_2 = sum(temp_list) / len(temp_list)
# print(temp_avg_2)

# highest_temp = data["temp"].max()
# print(highest_temp)

# Get data in columns
# print(data["condition"])
# print(data.condition)

# # Get data of row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# Convert Monday temperature to Fahrenheit
# monday_row = data[data.day == "Monday"]
# print(monday_row['temp'])
# fahrenheit = (monday_row['temp'] * 9/5) + 32;
# print(fahrenheit)

# Create a datafrom from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict);
print(data)
data.to_csv("new_data.csv")
