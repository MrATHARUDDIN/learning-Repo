fruits =        ["Apple", "Orange ", "banana"]
vegetables =    ["celery", "cucumber ", "carrots"]
Meats =         ["chicken", "fish", "turkey"]


#now this is a matrix of 3*3
groceries = [fruits , vegetables ,Meats]
print(groceries[0][0])


# print it like a matirx we just need 2 loop 
# One is for raw 
# One is for col
 

for x in groceries:
    print(x)
    for y in x:
        print(y , end=" ")
    print(" ")