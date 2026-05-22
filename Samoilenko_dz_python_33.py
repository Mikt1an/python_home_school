#1
import time

def meas_time(func):
    """
        Decorator that measures average execution time
        of a function over 5 runs.

        Args:
            func (function):
                Function to measure.

        Returns:
            function:
                Wrapped function with execution time measurement.

        Description:
            The decorator:
            - runs the function 5 times
            - measures execution duration for each run
            - calculates average execution time
            - prints the result

        Example:
            @meas_time
            def test():
                pass
        """
    def wrapper():
        total_time = 0
        result = None
        for _ in range(5):
            start = time.time()
            result = func()
            end = time.time()
            total_time += (end - start)
        average_time = total_time / 5
        print(f"Average execution time for 5 runs: {average_time:.2f} seconds")
        return result

    return wrapper

@meas_time
def compute():
    total = 0
    for i in range(10_000_000):
        total += i

    return total

print("Result:", compute())

# 2

def meas_time(repeats):
    """
        Creates a timing decorator with configurable
        number of repetitions.

        Args:
            repeats (int):
                Number of times the function should run.

        Returns:
            function:
                Decorator function.

        Description:
            This is a parameterized decorator.

            Unlike the first version, it allows
            dynamic control over the number
            of benchmark runs.
    """
    def decorator(func):
        def wrapper():
            total_time = 0
            result = None
            for _ in range(repeats):
                start = time.time()
                result = func()
                end = time.time()
                total_time += (end - start)
            average_time = total_time / repeats
            print(f"Average execution time for {repeats} runs: {average_time:.2f} seconds")
            return result

        return wrapper
    return decorator

@meas_time(10)
def compute():
    total = 0
    for i in range(10_000_000):
        total += i

    return total

print("Result:", compute())