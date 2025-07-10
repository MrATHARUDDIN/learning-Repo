import pandas as pd

# First data set
mydataset = {
    "cars":["Bmv","vocksbagan","Ford"],
    "passings":[3,7,2]
}

myvar = pd.DataFrame(mydataset)
print(myvar)

# print current version of pandas
print(pd.__version__)



# Pandas Series     
# Series is like column in a table so print all in a column
a = [1,6,7,3,5]
myseries = pd.Series(a)
print(myseries[1])
print(myseries) # it will also print the data type




# Create Labels
# with the "index" argument we can name our own lables

b = [1,7,2]
myvar = pd.Series(b,index=["x","y","z"])
print(myvar) 
# print(myvar[0]) # give us error
 
print(myvar["y"]) # we can access the value with our own index name
# note :- the index size of the matrix/array need to be same as number of the index it gonna declear


# create a Series from a dictionary, but include only some keys by specifying an index
calories = {"day1": 420, "day2": 380, "day3": 390}
cal_var = pd.Series(calories, index=["day1","day2"]) # only "day1" and "day2" will be included in the series
print(cal_var)