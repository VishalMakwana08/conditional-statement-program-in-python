
# Write a calculator using if-elif-else (supports +, -, *, /).

# Input: two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Input: operator
operator = input("Enter operation (+, -, *, /): ")

# Calculation using if-elif-else
if operator == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operator == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operator == "*":
    result = num1 * num2
    print(f"{num1} x {num2} = {result}")
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} ÷ {num2} = {result}")
    else:
        print("Error: Division by zero is not allowed ")
else:
    print("Invalid operator! Please enter +, -, *, or /")
