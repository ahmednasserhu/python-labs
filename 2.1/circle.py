from shape import Shape
import math

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__('Circle', color)
        self.radius = radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2) 