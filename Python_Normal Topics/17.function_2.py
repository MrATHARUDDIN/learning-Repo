#default arguments
import time

def net_price(list_price, discout=0, tax=0.05):
    return list_price * (1- discout) * (1 + tax)

print(net_price(500))             # Uses default discount = 0, tax = 0.05
print(net_price(500, 0.1))        # discount = 10%, tax = default 5%
print(net_price(500, 0.05, 0))    # discount = 5%, tax = 0



def count(start=0,end=3):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("Done!")

count()


## Keyworld

def hello(greating,title,first,last):
    print(f"{greating} {title} {first} {last}")


#You provide values in the same order as parameters are defined.
# Positional Arguments
hello("hello","Mr." ,"Spongebob" ,"Squarepants")

#Keyword Arguments Orders don't matter
hello(title="Mr. ", greating="Good Morning", first="Athar" , last="Uddin")

def getphone(country,area, first,last):
    return f"{country}-{area}-{first}-{last}"

phone_number = getphone(country=880,area=18,first=7406,last=1525)
print(phone_number)