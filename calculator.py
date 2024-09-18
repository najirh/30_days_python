# Project 1: Simple Calculator
"""
Mini Projects:
Create a function-based calculator that can perform basic operations like addition, subtraction, multiplication, and division. 
The user will enter two numbers and the operation (as a string, e.g., 'add', 'multiply'). 
Based on the input, call different functions to perform the operation and return the result.
"""


# add = +
# sub = -
# mul = *
# division = /


# addition
def add(num1, num2):
    return num1 + num2

# sub
def sub(num1, num2):
    return num1 - num2

# multiplication
def mul(num1, num2):
    return num1 * num2

# division
def div(num1, num2):
    return num1 / num2

def calculator(num1, num2, operation):
    
    if operation == 'add':
        result = add(num1, num2)
        
    elif operation == 'sub':
        result = sub(num1, num2)
        
    elif operation == 'mul':
        result = mul(num1, num2)
        
    elif operation == 'div':
        result = div(num1, num2)
        
    else:
       result = print("Please choose correct operation add, sub, mul, div!")
        
        
    return print(f"{num1} {num2} = {result}")

        
# execution of this application

if __name__ == "__main__":
    num1 = int(input("Please enter number1 :"))
    num2 = int(input("Please enter number1 :"))
    operation = input("Choose: add, sub, mul, div :")
    
    result = calculator(num1, num2, operation)
    print(result)

    