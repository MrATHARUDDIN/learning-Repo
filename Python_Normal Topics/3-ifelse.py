# Input age
age = int(input("Enter your age: "))
has_ticket = True  # Boolean variable
price = 10.00  # Base ticket price

# Age-based conditions
if age < 0:  # Fun condition
    print("You haven't existed yet!")
elif age == 0:  # Fun condition
    print("You are just born!")
elif age >= 65:
    print("You are a Senior Citizen")
    print(f"The ticket price for a Senior Citizen is ${price * 0.25}")  # 75% discount
elif age >= 18:
    print("You are an Adult")
    print(f"The ticket price for an Adult is ${price}")  # Full price
else:
    print("You are a Minor")
    print(f"The ticket price for a Minor is ${price * 0.50}")  # 50% discount

# Ticket section
if has_ticket:
    print("You may enter.")
else:
    print("You need to buy a ticket.")

# Explanation:
# - `if-elif-else` conditions are used to categorize age groups.
# - Fun conditions added for non-existing and newborn cases.

