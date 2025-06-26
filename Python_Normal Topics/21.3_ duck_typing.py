# 🦆 What is Duck Typing?
# "If it looks like a duck, swims like a duck, and quacks like a duck — then it’s a duck."

# In programming terms:
# If an object behaves like the expected type, you don’t need to care what its actual class is.
# Python is a dynamically typed language, so types are checked at runtime, not during variable declaration.

class Duck:
    def quack(self):
        print("Quack quack!")

class Person:
    def quack(self):
        print("I'm pretending to be a duck!")

def make_it_quack(thing):
    thing.quack()  # Doesn't care if it's a Duck or Person

d = Duck()
p = Person()

make_it_quack(d)  # Quack quack!
make_it_quack(p)  # I'm pretending to be a duck!