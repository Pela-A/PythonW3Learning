# Date data types do not exist in python by default
# NOTE that when working with formatting datetime objects we are not going to be able to memorize them all for now just look at documentation

# datetime module is a module we can use for working with dates as objects
import datetime
x = datetime.datetime.now()
print(x) # 2025-08-17 22:15:03.729616

# Return specific formats/information
print(x.year)
print(type(x))

# Date codes
print(x.strftime("%A"))    # Sunday (full weekday name)
print(x.strftime("%a"))    # Sun (abbreviated weekday)
print(x.strftime("%B"))    # August (full month name)  
print(x.strftime("%b"))    # Aug (abbreviated month)
print(x.strftime("%Y"))    # 2025 (4-digit year)
print(x.strftime("%y"))    # 25 (2-digit year)
print(x.strftime("%m"))    # 08 (month as zero-padded number)
print(x.strftime("%d"))    # 17 (day as zero-padded number)

# Time Codes
print(x.strftime("%H"))    # 14 (hour 24-hour format)
print(x.strftime("%I"))    # 02 (hour 12-hour format)
print(x.strftime("%M"))    # 30 (minutes)
print(x.strftime("%S"))    # 45 (seconds)
print(x.strftime("%p"))    # PM (AM/PM)


# Different date formats
print(x.strftime("%m/%d/%Y"))        # 08/17/2025
print(x.strftime("%B %d, %Y"))       # August 17, 2025
print(x.strftime("%A, %B %d, %Y"))   # Sunday, August 17, 2025

# Different time formats  
print(x.strftime("%H:%M:%S"))        # 14:30:45
print(x.strftime("%I:%M %p"))        # 02:30 PM

# Combined date and time
print(x.strftime("%Y-%m-%d %H:%M:%S"))           # 2025-08-17 14:30:45
print(x.strftime("%A, %B %d, %Y at %I:%M %p"))  # Sunday, August 17, 2025 at 02:30 PM

# TO SEE ALL RULES VISIT
# https://www.w3schools.com/python/python_datetime.asp

# Create a date using datetime constructor
# Require year month day
import datetime
# x = datetime.datetime(2020, 5, 17)
x = datetime.datetime(year=2020, month=5, day=17)

print(x)