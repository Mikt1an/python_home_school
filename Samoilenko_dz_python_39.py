# 1
import math
from abc import ABC, abstractmethod


class InvalidSizeError(Exception):
    """
        Custom exception for invalid shape dimensions.
    """
    pass


class Shape(ABC):
    """
        Abstract base class for geometric shapes.
    """
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    """
       Circle shape implementation.
    """
    def __init__(self, radius):
        if radius <= 0:
            raise InvalidSizeError(f"class {self.__class__.__name__} Radius must be positive")
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    """
        Rectangle shape implementation.
    """
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise InvalidSizeError(f"class {self.__class__.__name__} width or height must be positive")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


try:
    shapes = [Circle(3), Rectangle(4, 5)]
    Rectangle(-1,4)
    for shape in shapes:
        print(f"Area {shape.__class__.__name__}: {shape.area():.2f}")
except InvalidSizeError as e:
    print(f"Area: {e}")