print("I like Pizza")

# Variable Types - 1
age = 16  # int
full_name = "Athar Uddin"  # string (corrected variable naming style)
student = True  # bool (only True or False)
pi = 3.1416  # float (number with decimals)

print(f"My age is {age}")
print(f"My name is {full_name}")

if student:
    print("You are a student")
else:
    print("You are not a student")



# Arithmetic Operations - 2
friends = 5

friends = friends - 1  # 4
friends -= 1  # 3
friends += 2  # 5
friends = friends + 2  # 7
friends *= 2  # 14
friends = friends * 2  # 28
friends = friends / 5  # 5.6 (float result)
friends = friends % 2  # 1.6 (Incorrect, modulo only works for whole numbers)
friends = friends // 1.5  # 1 (floor division gives only whole numbers)

print(friends)

# Typecasting - 3
name = "bro code"
age = 25
is_student = True
gpa = 3.2

print(gpa)
gpa = int(gpa)  # Converts float to int (loses decimal)
print(gpa)

age = float(age)  # Converts int to float
age = age / 3
print(age)

age = str(age)  # Converts float to string
print(age)

# The following line is incorrect:
# age += 1  # Cannot add int to string, will raise TypeError

# Correct way to increment age after converting to string
age = float(age)  # Convert back to float
age += 1
print(age)

age = str(age) + "1"  # Concatenation (not addition)
print(age)

name = bool(name)  # Any non-empty string converts to True
print(name)
