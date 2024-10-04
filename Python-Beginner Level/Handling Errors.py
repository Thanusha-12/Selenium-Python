def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except TypeError:
        print("Error: Invalid input type. Please provide numbers.")
    else:
        print(f"The result is: {result}")
    finally:
        print("Execution complete.")
divide_numbers(10, 2)
divide_numbers(10, 0)
divide_numbers(10, 'a')

#File Handling
def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except IOError:
        print("Error: An I/O error occurred.")
    finally:
        print("File reading operation complete.")
read_file("existing_file.txt")
read_file("non_existent_file.txt")

#Input Validation
def get_integer_input():
    while True:
        try:
            value = int(input("Please enter an integer: "))
            return value
        except ValueError:
            print("Error: That's not an integer. Please try again.")
        finally:
            print("Input attempt complete.")
user_value = get_integer_input()
print(f"You entered: {user_value}")


