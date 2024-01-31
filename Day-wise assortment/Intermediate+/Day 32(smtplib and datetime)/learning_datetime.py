import datetime as dt

now = dt.datetime.now()  # If no argument give it gives info of our current timezone
# print(now)
year = now.year
month = now.month
day = now.day
week_day = now.weekday()  # Note 0 stands for Monday and so on
print(week_day)