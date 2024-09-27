# Return factorial of a number

def factorial(number):
    if number == 1:
        return 1
    else:
        return number * factorial(number - 1)

print("Input put a number to find its factorial.")

while True:
    try:
        number = int(input("Number: "))
        print('The factorial of {} is {}'.format(number, factorial(number)))
        break
    except:
        print('Please input an integer.')