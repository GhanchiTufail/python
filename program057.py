# program 57 :


# Define a custom exception class which takes a string message as attribute.


class MyError(Exception):
    def __init__(self, msg):
        self.msg = msg

try:  
    print(5/0)
except ZeroDivisionError:
    print("Divide by zero")
except Exception:
    print("caught an Exception")
finally:
    print("In finally block for cleanup")