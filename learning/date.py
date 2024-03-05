import datetime as dt
now = dt.datetime.now()
print (now)

print (now.year)
print (now.month)
print (now.day)
print (now.hour)
print (now.minute)
print (now.weekday())

# Create object which stores date time
date_of_birth = dt.datetime(year=1999, month=9, day=9)

print (date_of_birth)