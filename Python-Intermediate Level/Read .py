#READ operation
file = open("test for R&W")
#print(file.read()) #read the txt with specific characters
print(file.readline())
# print(file.readline())
#
# #print line by line by using while loop
#
# line = file.readline()
# while line !="":
#     print(line)
#     line = file.readline()
#
# # other way
# for line in file.readlines():
#     print(line)
#
# file.close()
#
# #need to learn skip function to skip the particular lines
# import itertools
# with open ('file text','r') as f:
#     next(f)
#     for line in f:
#         print(line)

# Writing binary data to a file
data = bytearray([120, 3, 255, 0, 100])  # Sample binary data

with open('../example.bin', 'wb') as binary_file:
    binary_file.write(data)

print("Binary data written to example.bin")

# Reading binary data from a file
with open('../example.bin', 'rb') as binary_file:
    data = binary_file.read()  # Read all binary data

print("Binary data read from example.bin:", list(data))

# Write some initial binary data
initial_data = bytearray([10, 20, 30, 40, 50])

with open('../example.bin', 'wb') as binary_file:
    binary_file.write(initial_data)

# Read and display the initial binary data
with open('../example.bin', 'rb') as binary_file:
    print("Before appending:", list(binary_file.read()))

# Append new binary data
new_data = bytearray([60, 70, 80])

with open('../example.bin', 'ab') as binary_file:
    binary_file.write(new_data)

# Read and display the content after appending
with open('../example.bin', 'rb') as binary_file:
    print("After appending:", list(binary_file.read()))


