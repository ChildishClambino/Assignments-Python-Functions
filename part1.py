# Task 1: Create functions for each arithmetic operation.number
# a = 2
# b = 3
# def addition(a, b):
#     return a + b   
# def subtraction(a, b):
#     return a - b
# def multiplication(a, b):
#     return a * b
# def division(a , b):
#     return a / b    

# Task 2: Implement user input to receive numbers and an operation choice.
# a = input("choose the first number that you want to add: ") 
# b = input("choose the second number that you would like to add: ")
# a = int(a)
# b = int(b)
# def addition(a, b):
#     print(a + b)
# addition(a, b)
   
# a = input("choose the first number that you would like to subtract: ")
# b = input("choose the second number that you would like to subtract: ")
# a = int(a)
# b = int(b)
# def subtraction(a, b):
#     print(a - b)
# subtraction(a, b)

# a = input("choose the first number that you want to multiply: ")
# b = input("choose the second number that you would like to multiply: ")
# a = int(a)
# b = int(b)
# def multiplication(a, b):
#     print(a * b)
# multiplication(a, b)
# Task 3: Ensure your program can handle division by zero and other potential errors.
a = input("choose the first number you would like to divide: ")
b = input("choose the second number you would like to divide by: ")
a = int(a)
b = int(b)
def division(a , b):
    if b == 0:
        print("Error: Cannot divide by zero")
    else:
        print(a / b)
division(a, b)

