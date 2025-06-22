# Python Classes/Objects
# Python is an object oriented programming language.
# Almost everything in Python is an object, with its properties and methods.
# A Class is like an object constructor, or a "blueprint" for creating objects.

class person:
    def __init__(self,name,age): # self Refers to current object
        # variable
        self.name = name
        self.age = age

    def greet(self): # method
        print(f"Hi, I'm {self.name} and I'm {self.age} years old.")

    def is_adult(self):
        if self.age >= 18:
            print("Yes you are adult")
        else:
            print("No You are not adult")



# Create an object
person1 = person("Athar", 17)

# Call a method
person1.greet()
person1.is_adult()