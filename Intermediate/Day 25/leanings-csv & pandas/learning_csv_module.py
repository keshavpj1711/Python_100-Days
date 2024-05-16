import csv

# # We can open csv files in a normal way but.
# # the representation of our tabular data won't be useful
# # See below
# with open("weather_data.csv", 'r') as weather_report:
#     # To read the file as a single string
#     # weather_report_data = weather_report.read()
#     # But when we usually want to work with the data we need to use readlines()
#     weather_report_data = weather_report.readlines()
#     print(weather_report_data)
#     # Now as you can see this prints the data in a very raw format and,
#     # this is not very easy to look at so what we do is
#     # We use csv module

# Using the csv modules to work with csv files
with open("weather_data.csv") as weather_report_file:
    weather_report_data = csv.reader(weather_report_file)

    print(weather_report_data)
    # This print statement gives us weird stuff because of csv.reader() read about it and you will know

    # Extracting the temp
    temperature = []

    # Printing the data in csv file
    for i in weather_report_data:
        print(i)
        temperature.append(i[1])

    # Printing the temperature separately
    print(temperature)

# Now this is not the best thing when you want to work with huge datasets,
# For which we have Pandas
