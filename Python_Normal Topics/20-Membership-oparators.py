# Membership Oparators = use to test a value or variable is found
# in a sequence (string, list,tuple, set or dictionary)
#                   1.In
#                   2.not In

main_name = "Athar"
print("A" in main_name) #true
print("C" in main_name) #False

list_num = [1,2,3,4,5,6,7,8]
print(7 in list_num , "Number Founded ") #Ture

tuple=('CodingNinjas', 'is', 'the', 'best', 'platform')
print("CodingNinjas" in tuple) #true
print("Coding Ninjas Studio" in tuple) #false

set_iteam = {"apple","orange","banana","coconut"}
print("apple" in set_iteam) #true
print("Apple" in set_iteam) #false