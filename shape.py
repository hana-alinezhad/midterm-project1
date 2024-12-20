# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 19:23:15 2024

@author: Hana
"""
import math

class shape:
    def __init__(self,name):
        self.name=name
    def area(self):
        return None
    def primeter(self):
        return None
    def __str__(self):
        return f"Shape name:{self.name},area:{self.area()},perimeter:{self.primeter()}"
    
class Triangle(shape):
    def __init__(self,base,height,side_a=None,side_b=None,side_c=None):
            shape.__init__(self,"triangle")
            self.base= base
            self.height= height
            self.side_a = side_a
            self.side_b = side_b
            self.side_c = side_c
    def area(self):
            return 0.5 * self.base *self.height
    def primeter(self):
            if self.side_a is not None and self.side_b is not None and self.side_c is not None:
                return self.side_a + self.side_b + self.side_c
            else:
                return "There is not anough valid information!"
class Circle(shape):
    def __init__(self,radius):
            shape.__init__(self,"circle")
            self.radius = radius
    def area(self):
            return math.pi *(self.radius**2)
    def perimeter(self):
            return 2*math.pi*self.radius
        
#usage

triangle = Triangle(base=10 , height =5 , side_a = 5 , side_b = 12 , side_c = 13)
circle = Circle(radius = 10)
print(triangle)
print(circle)
            
            
            
            
            
            
    