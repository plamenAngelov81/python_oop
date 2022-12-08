class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        area = Circle.pi * (self.radius ** 2)
        return area

    def get_circumference(self):
        c = 2 * Circle.pi * self.radius
        return c

    def set_radius(self, new_radius):
        self.radius = new_radius


circle = Circle(10)
circle.set_radius(12)
print(circle.get_area())
print(circle.get_circumference())
