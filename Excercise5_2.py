"""
5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. 
Once 'done' is entered, print out the largest and smallest of the numbers. 
If the user enters anything other than a valid number catch it with a try/except and put out an 
appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.
"""

largest_value = None
smallest_value = None
check=0

while True:
    value = input("Enter an integer number or 'done' for finish: ")

    try:
        if value != 'done':
            check = int(value)
        else:
            break
            
    except:
        print('Invalid input')
        continue

    if largest_value is None:
        largest_value = check
    if largest_value < check:
        largest_value = check

    if smallest_value is None:
        smallest_value = check
    if smallest_value > check:
        smallest_value = check

print('Maximum is', largest_value)
print('Minimum is', smallest_value)    
