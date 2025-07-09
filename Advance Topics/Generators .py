# A generator is a special type of function that remembers its state and yields values one at a time,
# instead of returning them all at once.

# Normal Function (returns a list) 

def fun():
    return [1,2,3]

nums = fun()
for i in nums:
    print(i)


# Generator Function (yields numbers)
def getnumber():
    yield 1
    yield 2
    yield 3

n = getnumber()
for i in n:
    print(i)

# 🔁 Notice: The generator version uses less memory because it doesn’t create the full list



#🔧 Real Use Case: Large Range
def count(max):
    count = 1
    while count <=max:
        yield count
        count += 1
for number in count(1000000):
    print(number)
