# Guess-the-number game

import random

print('Random number has been generated.')
num = int(random.random() * 100)
while True:
    try:
        guess = int(input('What is your guess? '))
        if guess < num:
            print('Too low')
            continue
        elif guess > num:
            print('Too high')
            continue
        else:
            print(f'Correct!! The number is {num}')
            break
    except ValueError:
        print('Please input an integer')