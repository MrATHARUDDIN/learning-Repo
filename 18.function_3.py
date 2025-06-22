# *args: For arbitrary positional arguments
# **kwargs: For arbitrary keyword arguments


def add(*args):
    toatl=0
    print(type(args)) #tuple
    for arg in args:
        toatl+=arg
    return toatl

print(add(5,3,3))

def print_adress(**pera):
    for key,value in pera.items():
        print(f"{key}: {value}")


print_adress(
    apt = "100",
    street="123 fake st.",
    city="Paris",
    state = "MI",
    Zip = "54321",
             )


def shipping_lable(*args, **kwargs):
    for arg in args:
       print(arg, end=" ")
    print()
    for value in kwargs.values():
      print(value, end=" ")
       

shipping_lable(
    "Dr.", "Athar", "Uddin", "III",
    street="123 fake st.",
    city="Paris",
    state = "MI",
    Zip = "54321",)