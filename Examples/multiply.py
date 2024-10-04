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






