from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius

    def calculate_area(self):
        circle_area = pi * self.__radius ** 2
        return circle_area

    def calculate_perimeter(self):
        circle_perimeter = 2 * pi * self.__radius
        return circle_perimeter


class Rectangle(Shape):
    def __init__(self, height, width):
        self.__height = height
        self.__width = width

    def calculate_area(self):
        area = self.__height * self.__width
        return area

    def calculate_perimeter(self):
        perimeter = 2 * (self.__height + self.__width)
        return perimeter


# circle = Circle(5)
# print(circle.calculate_area())
# print(circle.calculate_perimeter())
#
# rectangle = Rectangle(10, 20)
# print(rectangle.calculate_area())
# print(rectangle.calculate_perimeter())
