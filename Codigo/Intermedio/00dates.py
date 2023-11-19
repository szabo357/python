from datetime import datetime
from datetime import date
from datetime import time

now = datetime.now()

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())

print_date(now)

year_2023 = datetime(2023,1,1)

print_date(year_2023)

print(datetime.now())

# time
current_time = time(21, 6, 0)

print(current_time.hour)
print(current_time.minute)
print(current_time.second)