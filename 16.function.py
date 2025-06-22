def happy_birthday(name,age):
    print(f"happy bithday {name}")
    print(f"You are {age} years old now")

happy_birthday("athar",17)
happy_birthday("Steav",20)
happy_birthday("Jumur",45)

def display_invoice(username,ammout,due_date):
    print(f"hello {username}")
    print(f"you bill is ${ammout:.2f}")
    print(f"pay this Untail {due_date}")

display_invoice("brocode",120.45 ,"1/2")

# return function

# used to end a function ans send a result back to  the caller

def add(x,y):
    z = x + y
    return z

def subtrac(x,y):
    z = x-y
    return z

def multiply(x,y):
    z = x*y
    return z

def divide(x,y):
    z = x/y
    return z


print(add(1,2))