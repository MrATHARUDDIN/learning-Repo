def my_fun(contry):
    print(f"This is {contry} ") # we can also use maltipal peramitare

my_fun("Bangladesh")

def email(fname, lname):
  print(fname + "@" + lname + ".com")
email(str(input("Enter Your First name : ")),str(input("Enter Your Email Company name : "))) 
# we can also ask value from user



# To specify that a function can have only keyword arguments, add *, before the arguments:
# If more than 1. then add ** before peramiter/arguments
def my_function(**kid):
  print("His Pola is " + kid["pola"])

my_function(fname = "Tobias", lastname = "Refsnes", pola="Mustakim", nati="Dip")
