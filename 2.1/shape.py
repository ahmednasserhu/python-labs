from abc import ABC, abstractmethod

class Shape():
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def get_color(self):
        return self.color
    
    def set_color(self, color):
        self.color = color

    @abstractmethod
    def calculate_area(self):
        pass
