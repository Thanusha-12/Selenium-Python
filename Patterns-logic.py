#### Right-Angle Triangle #####
def right_angle_triangle(n):
    for i in range(1, n + 1):
        print('*' * i)
right_angle_triangle(7)

##### Right-Angle Triangle of Numbers ####
def right_angle_triangle_numbers(n):
    for i in range(1, n + 1):
        print(' '.join(str(j) for j in range(1, i + 1)))
right_angle_triangle_numbers(5)

######## Pyramid Pattern #####
def pyramid(n):
    for i in range(n):
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))
pyramid(5)

###### Pyramid of Numbers ####
def pyramid_numbers(n):
    for i in range(1, n + 1):
        print(' ' * (n - i) + ' '.join(str(j) for j in range(1, i + 1)))
pyramid_numbers(5)

#### Diamond Pattern ##
def diamond(n):
    for i in range(n):
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))
    for i in range(n - 2, -1, -1):
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))
diamond(5)

###### Inverted Pyramid ####
def inverted_pyramid(n):
    for i in range(n, 0, -1):
        print('*' * i)
inverted_pyramid(5)

###### Hallow Square #####
def hollow_square(n):
    for i in range(n):
        if i == 0 or i == n - 1:
            print('*' * n)
        else:
            print('*' + ' ' * (n - 2) + '*')
hollow_square(5)

####### Floyd's Triangle #####
def floyd_triangle(n):
    num = 1
    for i in range(1, n + 1):
        for j in range(i):
            print(num, end=' ')
            num += 1
        print()
floyd_triangle(5)






