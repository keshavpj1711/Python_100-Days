# Goal: Data Analysis
# We are going to analyze the squirrel census done in the central park new york
# The data we are going to use is already provided to us
# What we need to do is figure out how many of these squirrels are there of each color

# importing required modules or lib
import pandas


# Is there a way to work without copying the data in a variable
# Reading the data to in a variable
squirrel_census = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20231226.csv")

# Printing column names
# print(squirrel_census.columns)
# So since we are only interested in the Primary Fur color, therefore we only need that column
primary_fur_color = squirrel_census["Primary Fur Color"]

# Getting the total number of squirrels in the database
print(f"Total Squirrels: {len(primary_fur_color)}")


# This was to extract all the different fur colors in the csv file
# for i in primary_fur_color:
#     if i not in fur_color_list:
#         fur_color_list.append(i)

# Printing all the different colors present in the column
fur_color_dict = {
    'nan': {
        'count': 0,
    },
    'Gray': {
        'count': 0,
    },
    'Cinnamon': {
        'count': 0,
    },
    'Black': {
        'count': 0,
    }
}

# To get the dict keys as a list
fur_color_list = list(fur_color_dict.keys())
print(fur_color_list)

# To get the count of each fur color
for i in primary_fur_color:
    for j in fur_color_list:
        if i == j:
            fur_color_dict[j]["count"] += 1

print(fur_color_dict)
fur_color_data = pandas.DataFrame(fur_color_dict)
print(fur_color_data)
