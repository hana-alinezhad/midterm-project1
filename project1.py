class User:
        def __init__(self, username ,Ncode, password):
            self.username = username
            self.password = password
            self.Ncode = Ncode
            self.asdress = []
            self.cart = []
            self.is_logged_in = False
        
        def register(self):
            try:
                with open("project.txt", 'r') as file:
                    existing_member = set(line.split('@')[0] for line in file)
                while True:
                    self.Ncode = input("Enter you national code: ")
                    if self.Ncode in existing_member:
                        print("You have been registred.")
                    else:
                        break
                while True:
                    self.username = input("enter your username: ")
                    if self.username in existing_member:
                        print("This username is already taken.Choose another one.")
                    else:
                        break
                self.password = input("Write a password: ")
                with open("project.txt" , 'a') as file:
                    file.write(f"{self.Ncode}@{self.username}@{self.password}\n")
                print("Yoou have been registread successfully!")
            except:
                print("Error!!!") 
    
        def login(self , password ):
            if self.password == password:
                self.is_logged_in = True
                print(f"******{self.username} was logged in successfully.******")   
            else:
                print("Invalid password!Try again.")
    
        def logout (self):
            self.is_logged_in = False
            print("You logges out successfuly.")
        
        def address (self , address):
            try:
                if self.is_logged_in:
                    self.address.append(address)
                    print("Address was saved.")
                else:
                    print("At first login!")
            except:
                print("!!ERROR!!")


class Shopping:
        def __init__(self):
            self.products  = []

        def add(self , product , quantity):
            if product.stock >= quantity:
                if product in self.products:
                    self.products[product] += quantity
                else:
                    self.products[product] = quantity
                    product.stock -= quantity
            else:
                print("!!!Not enough stock!!!")
    
    


class Product :
        def __init__(self, name , price , stock):
            self.name = name 
            self.price = price
            self.stock = stock
        def update_stock(self,quantity):
            self.stock += quantity
        def __str__(self):
            return f"{self.name}@ price:{self.price} , @ stock :{self.stock} "
        
class Admin(User):
        def __init__(self , username , passcode):
            super().__init__(username , passcode)

        def add_pro(self,products , product):
            products.append(product)
            print("***This product is added successfully.***")

        def del_pro(self,products , product):
            products.remove(product)
            print("***This product is deleted successfully***")

