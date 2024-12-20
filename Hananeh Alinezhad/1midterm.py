class Tredmil:
    def __init__(self, first_name: str, last_name: str, weight: float, height: float):
        self.first_name = first_name
        self.last_name = last_name
        self.weight = weight
        self.height = height
    
    def print_name(self):
        print(f"first name is {self.first_name.lower()}")
        print(f"last name is  {self.last_name.upper()}")


class differences (Tredmil):
    def __init__(self, first_name: str, last_name: str, weight: float, height: float):
        Tredmil.__init__(first_name, last_name, weight, height)
        self.speed = 0  
        
    def increase_speed(self, increment: float):
        self.speed += increment
        print(f"your speed increased to {self.speed} ")
        
    def decrease_speed(self, decrement: float):
        self.speed = max(0, self.speed - decrement) 
        print(f" your speed decreased to {self.speed}")
    
   
    def get_speed(self):
        return self.speed
    def set_speed(self, speed: float):
        if speed >= 0:
            self.speed = speed
            print(f" speed {self.speed} ")
        else:
            print(" speed can not be negative!")


t1 = Tredmil("Ali ", "Mohammadi ", 76, 180)
t1.print_name()
