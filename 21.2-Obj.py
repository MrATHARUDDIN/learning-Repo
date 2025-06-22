
#Noob
class grandpa:
        car = "BMW"
        money = "100k"
        home= "ok"

class dad(grandpa):
    NoHome = ""
    Phone= "Iphone"

b = dad()
print(dad.car)


#Pro
class Grandpa:
    def __init__(self):
        self.car = "BMW"
        self.money = "100k"
        self.home = "ok"

class Dad(Grandpa):
    def __init__(self):
        super().__init__()  # Call Grandpa's __init__
        self.no_home = ""
        self.phone = "iPhone"
class Son(Dad):
     def __init__(self):
          super().__init__() # Call Dad
          self.laptop = "Macbook"
     def show_all(self):
        print("Car:", self.car)
        print("Money:", self.money)
        print("Home:", self.home)
        print("No Home:", self.no_home)
        print("Phone:", self.phone)
        print("Laptop:", self.laptop)

b = Dad()
print(b.phone)   # Output: BMW

s = Son()
print(s.show_all())
