### The Second Heighest Number in a List####
def second_highest(numbers):
    if len(numbers) < 2:
        raise ValueError("List must contain at least two numbers.")
    unique_numbers = list(set(numbers))
    if len(unique_numbers) < 2:
        raise ValueError("List must contain at least two distinct numbers.")
    unique_numbers.sort(reverse=True)
    return unique_numbers[1]
numbers = [1, 8, 4, 6, 8, 10]
print("The Second Heighest Number is",second_highest(numbers))

####### Even or Odd ########
num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))

########### Fibonacci #############
# """Return the nth Fibonacci number using iteration."""
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
n = 10
print(fibonacci(n))

# """Return the nth Fibonacci number using recursion."""
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
n = 10
print(fibonacci_recursive(n))

# """Return the nth Fibonacci number using dynamic programming."""
def fibonacci_dp(n):
    if n <= 1:
        return n
    fib = [0] * (n + 1)
    fib[1] = 1
    for i in range(2, n + 1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib[n]
n = 10
print(fibonacci_dp(n))

# """Return a list of the first n Fibonacci numbers."""
def fibonacci_list(n):
    fib_list = []
    a, b = 0, 1
    for _ in range(n):
        fib_list.append(a)
        a, b = b, a + b
    return fib_list
n = 10
print(fibonacci_list(n))

######################### Reverse a string ###########
# """Reverse a string using slicing."""
def reverse_string(s):
    return s[::-1]
original_string = "hello"
reversed_string = reverse_string(original_string)
print(reversed_string)  # Output: "olleh"

# """Reverse a string using a loop."""
def reverse_string_loop(s):
    reversed_string = ""
    for char in s:
        reversed_string = char + reversed_string
    return reversed_string
original_string = "hello"
reversed_string = reverse_string_loop(original_string)
print(reversed_string)  # Output: "olleh"

# """Reverse a string using reversed() and join()."""
def reverse_string_reversed(s):
    return ''.join(reversed(s))
original_string = "hello"
reversed_string = reverse_string_reversed(original_string)
print(reversed_string)  # Output: "olleh"

#"""Reverse a string using a stack (list)."""
def reverse_string_stack(s):
    stack = list(s)
    reversed_string = ''
    while stack:
        reversed_string += stack.pop()
    return reversed_string
original_string = "hello"
reversed_string = reverse_string_stack(original_string)
print(reversed_string)  # Output: "olleh"



