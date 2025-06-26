# Collection-Type	Syntax	Ordered	    Changeable	    Allows Duplicates
#List	              []	✅	        ✅	          ✅
#Set	              {}	❌	        ✅	          ❌ (no duplicates)
#Tuple	              ()	✅	        ❌ (immutable) ✅


#---------------------------------------------------------------------------------------#


fruits = ["apple", "orange", "banana"] # it like actually array

print(fruits[0]) # index number\
# print(fruits[4]) that will give us an syntax error

for fruit in fruits:
    print(fruit)


#---------------------------------------------------------------------------------------#
# Set = {} → unordered, changeable, no duplicates
fruits_set = {"lol", "fuck", "banana", "apple"}  # duplicate "apple" will be removed automatically

# print(fruits_set[0]) → ❌ Error: set is unordered, no indexing

for fruit in fruits_set:
    print(fruit)  # Order is not guaranteed

#---------------------------------------------------------------------------------------#


# Tuple = () → ordered, not changeable, allows duplicates
fruits_tuple = ("apple", "orange", "banana", "apple")

print(fruits_tuple[0])  # Access by index → "apple"

for fruit in fruits_tuple:
    print(fruit)


