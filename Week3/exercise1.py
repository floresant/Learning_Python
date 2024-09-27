# Function to check if string is a palindrome

def palidrome_check(string):
    half = len(string) // 2

    # Loop through string comparing beginning and end up to half-point
    j = -1
    for i in range(0, half):
        front = string[i].lower()
        rear = string[j].lower()
        if front != rear:
            print(f'Your string: \n\t{string} \nis not a palindrome.')
            break
        else:
            j -= 1
    else:
        print(f'Your string: \n\t{string} \nis a palindrome!')

msg = input("What is your text? ")
palidrome_check(msg)
