##Lambda
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61] #22,54,62
even_numbers = list(filter(lambda x: x % 2 == 0, li))
print(even_numbers)

multiplied_list = list(map(lambda x: x * 2, li))
print(multiplied_list)



## Rectangele calculate the area=width*length using data abstraction
#
# class Rectangle():
#     def __int__(self,width,length):
#         self.width = width
#         self.length = length
#     def area(self):
#         return self.width * self.length
#     def main():
#         width = float(input("Enter the width of the rectangle: "))
#         length = float(input("Enter the length of the rectangle: "))
#         rect = (width, length)
#         print(f"The area of the rectangle is: {rect.area()}")
#     if __name__ == "__main__":
#         main()

# String = "I am  a thanusha" remove a from the string and give output as I am thanusha in a string format in python

my_string = "I am a thanusha"
new_string = my_string[0:4] + my_string[6:15]
print(new_string)  # Output: I am thanusha

#  print "Welcome to python" by using decorators and clousers

def decorator_function(function):
    def inner_function():
        print("Welcome to Python")
        function()
    return inner_function
@decorator_function
def print_message():
    pass
print_message()

def outer_function(fun):
    def decorator_function(function):
            print("Text")
    return decorator_function
def say_hello():
    print("POC Review")

say_hello()

def outer_function(message):
    def inner_function():
        print(message)
    return inner_function
print_message = outer_function("Welcome to Python")
print_message()


# get the word "Batman" from the sentence "The Adventure of Batman" by using patterns

import re
Text = "The Adventure of Batman"
pattern = r"\bBatman\b"
match = re.search(pattern, Text)
if match:
    print("Matched word:", match.group())
else:
    print("Word not found")

#to print 100 characters from  the text file by using slice

def read_first_100_chars(text):
    try:
        with open(text, 'r') as file:
            content = file.read()
            print(content[:100])
    finally:
        print("text")
text = 'message'
read_first_100_chars(text)


search_box_xpath = "//input[@id='twotabsearchtextbox']"
search_box.send_keys("mobiles")

".//span[contains(@class, 'a-price-whole')]"










