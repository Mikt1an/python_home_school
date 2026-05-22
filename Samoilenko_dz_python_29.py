# 1

def fibonacci_gen():
    """
        Infinite Fibonacci sequence generator.

        Yields:
            int: The next number in the Fibonacci sequence.

        Description:
            This generator produces Fibonacci numbers endlessly using the
            `yield` keyword. Each new number is calculated as the sum of
            the previous two numbers.

        Fibonacci sequence example:
            0, 1, 1, 2, 3, 5, 8, 13, ...

        Variables:
            a (int): Current Fibonacci number.
            b (int): Next Fibonacci number.

        Example:
            fibonacci = fibonacci_gen()

            for _ in range(5):
                print(next(fibonacci))

            Output:
                0
                1
                1
                2
                3
        """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fibonacci = fibonacci_gen()
for i in fibonacci:
    input_next = input("Enter to step: ")
    if input_next == "q":
        break
    print(i)


# 2

data = [3, 1, 2, 3, 4, 1, 5, 2, 6, 7, 5, 8]

def unique_generator(item : list):
    """
        Generator that yields only unique elements from a list.

        Args:
            item (list):
                List containing elements that may include duplicates.
        Yields:
            int:
                Unique elements in the same order as their first appearance.

        Description:
            This generator removes duplicate values while preserving
            the original order of elements.

            A `set` is used to store already encountered values.
            If an element has not been seen before, it is added
            to the set and yielded.

        Example:
            data = [1, 2, 2, 3, 1, 4]

            unique = unique_generator(data)

            for i in unique:
                print(i)

            Output:
                1
                2
                3
                4
    """
    add_item =  set()
    for elem in item:
        if elem not in add_item:
            add_item.add(elem)
            yield elem

unique = unique_generator(data)
for i in unique:
    print(i)