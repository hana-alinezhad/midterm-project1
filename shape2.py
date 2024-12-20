# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 08:19:55 2024

@author: Hana
"""

import math

class Shape:
    def __init__(self, name):
        self.name = name
        
    def area(self):
        return None
    
    def perimeter(self):
        return None
    
    def __str__(self):
        return f"Shape name: {self.name}, area: {self.area()}, perimeter: {self.perimeter()}"
    
class Triangle(Shape):
    def __init__(self, base, height, side_a=None, side_b=None, side_c=None):
        super().__init__("triangle")
        self.base = base
        self.height = height
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        
    def area(self):
        return 0.5 * self.base * self.height
    
    def perimeter(self):
        if self.side_a is not None and self.side_b is not None and self.side_c is not None:
            return self.side_a + self.side_b + self.side_c
        else:
            return "There is not enough valid information!"
        
class Circle(Shape):
    def __init__(self, radius):
        super().__init__("circle")
        self.radius = radius
        
    def area(self):
        return math.pi * (self.radius ** 2)
    
    def perimeter(self):
        return 2 * math.pi * self.radius
        
# Usage
triangle = Triangle(base=10, height=5, side_a=5, side_b=12, side_c=13)
circle = Circle(radius=10)

print(triangle)
print(circle)
