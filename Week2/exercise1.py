# Inifitely loop until user provides an integer
while True:
    try:
        num = int(input("Number: "))
        break
    except ValueError:
        print("Please input an integer")

# Loop through all integers from 2 to num
for i in range(2, num):
    # Num is not a prime number if it modulus with any integer is 0
    if num % i == 0:
        print(f'{num} is not a prime number. {i} * {int(num / i)} = {num}')
        break
else:
    print(f'{num} is a prime number!')