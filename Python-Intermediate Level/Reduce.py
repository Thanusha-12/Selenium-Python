##Reduce is a function from the functools module that applies
# a binary function to an iterable (like a list) cumulatively, reducing it to a single value.
####Summing a List of Numbers
from functools import reduce
def add(x, y):
    return x + y
numbers = [1, 2, 3, 4, 5]
result = reduce(add, numbers)
print("The sum is:", result)

####Finding the Maximum Value
from functools import reduce
def max_value(x, y):
    return x if x > y else y
numbers = [10, 20, 4, 45, 99]
result = reduce(max_value, numbers)
print("The maximum value is:", result)

###Concatenating Strings
from functools import reduce
def concatenate(x, y):
    return x + y
strings = ["Hello", " ", "World", "!"]
result = reduce(concatenate, strings)
print("Concatenated string is:", result)


