##Variables defined within a function are local to that function
def my_function():
    x = 10  # x is local to my_function
    print(x)
my_function()
#Variables defined outside of any function are in the global scope.
y = 20  # y is global
def another_function():
    print(y)
another_function()

#In nested functions, a variable in the outer function can be accessed by the inner function.
def outer_function():
    z = 30
    def inner_function():
        print(z)
    inner_function()
outer_function()


