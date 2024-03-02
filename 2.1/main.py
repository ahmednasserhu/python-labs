from circle import Circle
from square import Square
from rectangle import Rectangle

circle = Circle('red', 5)
square = Square('blue', 5)
rectangle = Rectangle("green", 5, 5)

print("Area of Circle:", circle.calculate_area())
print("Area of Square:", square.calculate_area())
print("Area of Rectangle:", rectangle.calculate_area())