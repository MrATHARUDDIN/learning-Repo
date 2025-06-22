#while loop is use to repeat a block of code as long as the condition is true
# it check condition at the end of the loop if the condition is false the loop is over

# while 1 == 1:
#  print("Im stuck in a lopp!")

name = input("Enter your name :")
while name == "":
    name = input("Enter you name : ")

age = int(input("Enter you age :"))

while age < 18:
    print("age can't be less than 18")
    age = int(input("Enter you age :"))

print(f"Hello {name}!")
print(f"Your age {age}!")
    