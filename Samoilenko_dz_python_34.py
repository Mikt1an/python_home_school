# 1

class Rectangle:
    """
       Simple rectangle class for area calculation.
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height


rect = Rectangle(5, 10)
print("Area", rect.get_area())
rect.width = 100
rect.height = 50
print("", rect.get_area())


# 2

class Counter:
    """
        Simple counter class with increment and decrement operations.
    """
    def __init__(self):
        self.count = 0

    def count_up(self):
        self.count += 1
        print ("counter increased: ", self.count)

    def count_down(self):
        self.count -= 1
        print ("counter decreased: ", self.count)

    def total(self):
        return self.count

counter = Counter()
counter.count_up()
counter.count_down()
counter.count_down()
counter.count_down()
counter.count_down()
print("Current value:", counter.total())