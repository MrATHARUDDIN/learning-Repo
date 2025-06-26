# Random number Python
import random # need to  import this module


# range of 1 to 6
number = random.randint(1,6) 


# low to hight by variable
low = 1
high = 100
randomnumber = random.randint(low,high)

# options random
options = ("Rock", "paper","Scissors","Fire","Water")
option = random.choice(options)
print(option)