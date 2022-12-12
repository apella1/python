ival = input('Enter a numer: ')

try:
    ival = int(ival)
except:
    ival = -1

if ival > 0:
    print(f'{ival} was a great choice')
else:
    print(f'Not a number!')
    new_number = input('Please enter a number: ')
    ival = new_number