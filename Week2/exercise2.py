# Count up to a number by skipping by a number

while True:
    try:
        num = int(input("Input a number you would like to count to: "))
        break
    except ValueError:
        print("Please input an integer.")

while True:
    try:
        skip = int(input("Input what you would like to count by: "))
        break
    except ValueError:
        print("Please input an integer.")

for i in range(0, num, skip):
    print(i)
    if i + skip > num:
        print(f"Cannot count to {num} evenly by {skip}'s, stops at {i} with remainder {num - i}")
        break
