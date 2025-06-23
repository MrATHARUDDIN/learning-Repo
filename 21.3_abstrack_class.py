# An abstract class is a class that cannot be instantiated directly. It is meant to be inherited by other classes.
#  It can have abstract methods (methods with no implementation) that must be implemented by any subclass.

# Think of it as a template or blueprint for other classes.

from abc import ABC, abstractmethod


# class Animal:
#    def make_sound(self):
#        pass  # no enforcement, just a placeholder

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass  # this must be implemented in subclasses

class Dog(Animal):
    def make_sound(self):
        return "Bark"

class Cat(Animal):
    def make_sound(self):
        return "Meow"

dog = Dog()
print(dog.make_sound()) 


# Real life example
# Suppose you’re building an app that supports different payment gateways.


# Abstract base class
class PaymentGateway(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

# Concrete class: PayPal
class PayPal(PaymentGateway):
    def process_payment(self, amount):
        print(f"Processing ${amount} through PayPal")

# Concrete class: Stripe
class Stripe(PaymentGateway):
    def process_payment(self, amount):
        print(f"Processing ${amount} through Stripe")

# Using the classes
paypal = PayPal()
paypal.process_payment(100)  # ✅ Output: Processing $100 through PayPal

stripe = Stripe()
stripe.process_payment(150)  # ✅ Output: Processing $150 through Stripe



# Just a regular base class
class PaymentGateway:
    def process_payment(self, amount):
        pass  # just a placeholder, no enforcement

class PayPal(PaymentGateway):
    def process_payment(self, amount):
        print(f"Processing ${amount} through PayPal")

class Stripe(PaymentGateway):
    def process_payment(self, amount):
        print(f"Processing ${amount} through Stripe")

# Using the classes
paypal = PayPal()
paypal.process_payment(100)  # ✅ Works fine

stripe = Stripe()
stripe.process_payment(150)  
