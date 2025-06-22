car = ["BMW","Toyota","Bugadi","Honda"]
car.append("Porsh 911")
print(car)

car.append(str(input("Enter your brand name : ")))

for x in car:
    print(x)

car.pop(0) # remove the index 0 that means no more "BMW"
car.remove("Porsh 911") # also no more "Porsh 911"

car.insert(0, "Ferrari")  # Adds "Ferrari" at index 0
# you can add it anywhere you want
print(car)

new_cars = ["Lamborghini", "McLaren"]
car.extend(new_cars)  # Adds all items from new_cars to car
print(car)

  # Sorts the list alphabetically
car.sort()
print(car)


# car.reverse()    \\ only reverse the list \\
# print(car)
