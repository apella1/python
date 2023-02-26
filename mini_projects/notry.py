val = input('Enter a number: ')

try:
    val = int(ival)
except:
    val = -1

if val > 0:
    print(f'{val} was a great choice')
else:
    print(f'Not a number!')
    new_number = input('Please enter a number: ')
    val = new_number