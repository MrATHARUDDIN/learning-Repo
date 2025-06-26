# Will print numbers from 1 to 10
for x in range(1, 11):
    print(x)


# Will print numbers from 1 to 10 with 2 number increment (1, 3, 5, 7, 9)
for y in range(1, 11, 2):
    print(y)


# Will print each character of the credit card number one by one
credit_card = "1234-5678-9012-3222"
for x in credit_card:
    print(x)


# Will print numbers from 1 to 20, skipping number 13
for x in range(1, 21):
    if x == 13:
        continue
    else:
        print(x)

# Will print number 1 to 21 but stop at 12 because 
# when x == 13 break the loop
for x in range(1, 21):
    if x == 13:
        break
    else:
        print(x)