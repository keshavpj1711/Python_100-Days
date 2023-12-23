import pandas


# Printing our data in a much better format
weather_report_data = pandas.read_csv("weather_data.csv")
# print(weather_report_data)
# print(type(weather_report_data))
# the weather_report_data represents an object named dataframe


# Getting hold of only one column
# print("\nGetting hold of temp column")
temp_data = weather_report_data["temp"]
# Another way of doing this is:
# temp_data = weather_report_data.temp
# print(temp_data)
# When doing this
# print(type(temp_data))
# Similarly this represents an object named series


# Using pandas we can also change the data format
# Like changing ours to a dictionary
weather_report_dict = weather_report_data.to_dict()
# print(weather_report_dict)
# Our output dict
# {'day': {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'},
#  'temp': {0: 12, 1: 14, 2: 15, 3: 14, 4: 21, 5: 22, 6: 24},
#  'condition': {0: 'Sunny', 1: 'Rain', 2: 'Rain', 3: 'Cloudy', 4: 'Sunny', 5: 'Sunny', 6: 'Sunny'}}


# We can also change a separate series
# Suppose we wish to change temp_data to a list
temp_data_list = temp_data.tolist()
# print(temp_data_list)
# Output List
# [12, 14, 15, 14, 21, 22, 24]


# Printing out the average temperature
# sum_temp = 0
# for i in temp_data_list:
#     sum_temp += i
# avg_temp = round(sum_temp/len(temp_data_list), 2)
# print(f"\n Average Temp: {avg_temp} C")
# This is how you would normally approach your problem

# But with pandas you can find mean with just a simple fn call
print(f"\nAverage Temp: {round(temp_data.mean(), 2)} C")


# Getting the max value of temperature
print(f"\nMax Temp: {temp_data.max()}")


# Getting data in row
print("\nTemperature details for Tuesday")
tue_report = weather_report_data[weather_report_data.day == "Tuesday"]
print(tue_report)
# Let say we want to have the content of the row whose temp is max
# Comparing the temp with max temp and then giving that row data to max_day_report
max_day_report = weather_report_data[weather_report_data.temp == weather_report_data.temp.max()]
print("\nReport for day with max temp")
print(max_day_report)