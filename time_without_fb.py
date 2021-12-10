import datetime
first_time = "2021-12-10 12:47:45.567592"#datetime.datetime.now()


# datetime(year, month, day, hour, minute, second)
a = datetime.datetime(2021, 12, 10, 12, 47, 45)
b = datetime.datetime.now()
#b = datetime.datetime(2017, 5, 16, 8, 21, 10)
  
# returns a timedelta object
c = b -a
print('Difference: ', c)
  
minutes = c.total_seconds() / 60
print('Total difference in minutes: ', minutes)
  
# returns the difference of the time of the day
minutes = c.seconds / 60
print('Difference in minutes: ', minutes)
