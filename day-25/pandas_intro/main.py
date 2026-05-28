import pandas

data = pandas.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20260528.csv");

count_color = data["Primary Fur Color"].value_counts()
print(count_color)

data_frame = pandas.DataFrame(count_color)
data_frame.to_csv("color_count.csv")