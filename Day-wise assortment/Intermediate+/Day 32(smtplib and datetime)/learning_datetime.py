import datetime as dt

now = dt.datetime.now()  # If no argument give it gives info of our current timezone
# print(now)
year = now.year
month = now.month
day = now.day
week_day = now.weekday()  # Note 0 stands for Monday and so on
# print(week_day)

# Creating our own object
my_dob = dt.datetime(day=17, month=11, year=2003)
print(my_dob)