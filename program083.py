# program 83:

# Please write a program to print the running
# time of execution of "1+1" for 100 times.

# Hints:
# Use timeit() function to measure the running time.

from timeit import Timer
import datetime

time = Timer("for cnt in range(100):1+1")
print(time.timeit())

print(datetime.datetime(year=2003,month=6,day=5,hour=12,minute=50,second=35,microsecond=120000))

print(datetime.date())