# Iterable = An Object/Collection that can return its elemeents one at a time,
# allowing it to be iterated over in a loop

#list
number= [1,2,3,5,6,7]

for num in reversed(number):
    print(num , end=" ")

print()

# set
fruits = {"apple","orange","banana","coconut"}
for fruit in fruits:
    print(fruit)

#string
name = "Bro code"
for letters in name:
    print(letters)


#dictionary

my_dictionary ={
    "name" : "athar",
    "age" :17,
    "city": "noakhali"
}


for item in my_dictionary:
    print(item) #it will print all the keys

for items in my_dictionary.values():
    print(items) #it will print the value 

for info in my_dictionary.items():
    print(info) #it will print both keys and items

for key ,value  in my_dictionary.items():
    print(key) #it will print key
    print(value) #it will print value



