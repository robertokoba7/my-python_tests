#!/usr/bin/python3
#This is a list comprehension with functions.
#Create a function that retgurns a number doubled.

def doubled (x):
    return x*2

nums = [doubled (x) for x in range(1,10)]
print (nums)

#dd a fiter so we only doubleeven numbers.
even_nums = [doubled (x) for x in range(1,10) if x %2 == 0]
print(even_nums)
