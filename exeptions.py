class CustomException(Exception):
    def __init__(self, message):
        super().__init__(message)

try:

    result = 10 / 0
except ZeroDivisionError:
    print("Caught a ZeroDivisionError: Cannot divide by zero")

try:

    my_list = [1, 2, 3]
    print(my_list[5])
except IndexError:
    print("Caught an IndexError: Index out of range")

try:
    int_value = int("abc")
except ValueError:
    print("Caught a ValueError: Invalid conversion")

try:
 
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Caught a FileNotFoundError: File not found")

try:

    age = int(input("Enter your age: "))
    if age < 0:
        raise CustomException("Age cannot be negative")
except CustomException as ce:
    print(f"Caught a CustomException: {ce}")
else:
    print(f"Your age is {age}")

finally:
    print("This code always runs")

print("Program continues...")

