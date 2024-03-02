from shape import Shape

class Square(Shape):
    def __init__(self, color, side):
        super().__init__("Square", color)
        self.side = side

    def calculate_area(self):
        return self.side ** 2
