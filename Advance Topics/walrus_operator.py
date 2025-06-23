# The Walrus Operator := 🦦 is a handy feature introduced in Python 3.8. Here's a clean and clear explanation with examples.
# It is like shorthand of any Condition check or runing loops

# 🔁 Without Walrus Operator
data = input("Type anything : ")

if data != "":
    print(f"You entered: {data}")
else:
    print("type something ideat")

# ✅ With Walrus Operator
if (data := input("Enter something: ")) != "":
    print(f"You entered: {data}")
else:
    print("type something ideat")


# while loop with Walrus Operator
while (line := input("Type: ")) != "exit":
    print(f"You typed: {line}")

numbers = [5, 12, 8, 21, 3]



for x in numbers:
    if(x*2 >15):
        print(f"{x} doubled is is {x*2} , which is > 15")

for n in numbers:
    if (double := n * 2) > 15:
        print(f"{n} doubled is {double}, which is > 15")


# For loop we can't use it in for loop only for conditions
# And normaly we dont need that stuff for coding just to know and understand others programm
# that's all