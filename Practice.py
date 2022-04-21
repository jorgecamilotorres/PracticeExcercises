# This program request the user n numbers until the user type 'done' to Math the Total, Count and Average.
# If the user types a non integer number, the program prints the text 'bad data' and don't consider that input.

Total = 0
Count = 0

while True:
    data = input('Enter an Integer Number or Enter "done" to Finish: ')
    
    if data == 'done':
        break

    try:
        number = int(data)   
    except:
        print('bad data')
        continue

    Total = Total + number
    Count += 1

Average = Total/Count

print('total=', Total, 'Count=', Count, 'Average=', Average)