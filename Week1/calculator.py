# Add, subtract, multiply, and divide two numbers

# Loop infinitely until user provides a number
while True:
    try:
        num1 = float(input('First number: '))
        break
    except ValueError:
        print("Please input a number.")

while True:
    try:
        num2 = float(input('Second number: '))
        break
    except ValueError:
        print("Please input a number.")

operation_list = ['+', '-', '*', '/']

# Loop infinitely until user provides proper operation
while True:
    operation = input('What is the operation (+, -, *, or /)? ')
    if operation in operation_list:
        break
    else:
        print("Please input +, -, *, or / as an operation.")

if operation == "+":
    solution = num1 + num2
elif operation == "-":
    solution = num1 - num2
elif operation == '*':
    solution = num1 * num2
elif operation == '/':
    solution = num1 / num2

print(f'{num1} {operation} {num2} = {solution}')