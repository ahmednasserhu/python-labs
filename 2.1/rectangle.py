from shape import Shape

class Rectangle(Shape):
    def __init__(self, color, length, width):
        super().__init__("Rectangle", color)
        self.color = color
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.width * self.length