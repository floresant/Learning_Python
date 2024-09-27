# Slicing strings
## Method 1 - Using slice()
string = "A simple string"

s1 = slice(4)  # Start at beginning and stop before 4th index
s2 = slice(2, 8, 2)  # Start at index 2, stop before 8th index, include every 2nd character

print(string[s1])  # Prints "A si"
print(string[s2])  # Prints "sml" 

## Method 2 - Array method
print(string[:3])  # Prints "A si"

# Concatenating strings
## Using + operator
s3 = 'air'
s4 = 'plane'

print(s3 + s4)  # Prints 'airplane'

## Using join()
### This will concatenate string with a separator
print('Concatenated String using join() =', "".join([s3, s4]))
print('Concatenated String using join() and whitespaces =', " ".join([s3, s4]))
print('Concatenated String using join() and commas =', ",".join([s3, s4]))

## Using % operator
print("An %s%s probably weighs more than %d lbs." % (s3, s4, 100))

## Using format()
s5 = "{}{}".format(s3, s4)
print('String Concatenation using format() =', s5)
print('String Concatenation using format() = {in1}{in2}'.format(in1=s3, in2=s4))

# Formatting strings aka f-string
print(f'{s3} and {s4} together make {s3}{s4}')