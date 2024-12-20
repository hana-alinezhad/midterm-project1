class A:
    def __init__(self, name, age, job):
        self.__name = name  #privcy
        self._age = age     #protected
        self.job = job      #public

    def get_name(self):
        return self.__name  

    def get_age(self):
        return self._age   

# usage
person1 = A("Ali", 30, "Engineer")

print(person1.get_name())  
print(person1.get_age())   
print(person1.job)         

