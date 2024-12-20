# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 18:53:58 2024

@author: Hana

"""

class student:
    
    
    def __init__(self,name,student_id,major):
        self.name = name
        self.student_id = student_id
        self.major = major
        self.courses =[]
        
    def get_name(self):
        return self.name
    def set_name(self,name):
        self.name = name
    def get_student_id(self,name):
        return self.student_id
    def set_student_id(self,student_id):
        self.student_id = student_id
    def get_major(self):
        return self.major
    def set_major(self,major):
        self.major = major
        
        
    def add_course(self,course):
        if course in self.courses:
            self.courses.append(course)
            print(f"Course{course} was added successfully.")
        else:
            print(f"This course{course} is already taken.")
            
    def remove_course(self,course):
        if course in self.courses:
            self.courses.removed(course)
            print(f"Course{course} was removed successfully")
        else:
            print(f"Course {course} not found.")
            
    
    def __str__(self):
        return f"Name: {self.name}, Student ID: {self.student_id}, Major: {self.major}, Courses: {', '.join(self.courses)}"
  
    
  
student = student("Ali", "123456", "Computer Science")
print(student) 

student.add_course("Math") 
student.add_course("Physics") 
print(student) 

student.remove_course("Math")
print(student) 

student.remove_course("Biology")
    
    
    
    
            
        
        
        
    
        
    
