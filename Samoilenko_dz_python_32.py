# 1

def make_rounder(digit: int):
    """
        Returns a function that rounds numbers
        to the specified number of decimal places.
        """
    def round_number(number):
        return round(number, digit)

    return round_number

round2 = make_rounder(2)
round0 = make_rounder(0)


print(round2(3.14159))
print(round2(2.71828))
print(round0(9.999))

# 2
from datetime import datetime


def create_logger():
    """
        Creates a logger function that stores events with timestamps.

        Returns:
            function:
                Inner logging function.

        Description:
            This function demonstrates a closure in Python.

            The outer function creates a private list called `events`
            that stores all logged messages.

            The inner function:
            - adds new events with the current timestamp
            - returns the full event history

            Each created logger has its own independent event storage.

        Example:
            log = create_logger()
            log("Program started")
            log("File saved")

            print(log())

        Output Example:
            [
                'Program started: 2026-05-22 12:30:15',
                'File saved: 2026-05-22 12:31:02'
            ]
        """
    events = []

    def log(event=None):
        if event is not None:
            cur_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            events.append(f"{event}: {cur_time}")
        return events

    return log

log = create_logger()
log("DOWNLOAD DATE")
log("Processing completed")
log("Saving file")
for event in log():
    print(event)


# 3
#V1
def decorator(func):
    """
        Decorator function that adds visual separators
        before and after function execution.

        Args:
            func (function):
                Function to decorate.
        Returns:
            function:
                Wrapped function with additional behavior.

        Description:
            This decorator demonstrates the basic concept
            of decorators in Python.

            The wrapper function:
            - prints a separator line before execution
            - executes the original function
            - prints another separator line after execution

        Example:
            @decorator
            def hello():
                print("Hello")
            hello()
        Output:
            --------------------------------------------------
            Hello
            --------------------------------------------------
        """
    def wrapper():
        print("-"*50)
        func()
        print("-"*50)
    return wrapper


def say_hello():
    print("Привет, игрок!")

say_hello = decorator(say_hello)
say_hello()

#V2
def decorator(func):
    """
        Decorator that adds separator lines
        before and after function execution.

        Args:
            func (function):
                Function to decorate.
        Returns:
            function:
                Wrapped version of the original function.

        Description:
            This decorator demonstrates Python decorator syntax
            using the `@decorator` notation.

            The decorator:
            - prints a separator before function execution
            - runs the original function
            - prints another separator after execution

        Example:
            @decorator
            def hello():
                print("Hello")
            hello()
    """
    def wrapper():
        print("-"*50)
        func()
        print("-"*50)
    return wrapper

@decorator
def say_hello():
    print("Привет, игрок!")

say_hello()