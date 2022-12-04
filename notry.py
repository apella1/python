ival = input('Enter a numer: ')

try:
    ival = int(ival)
except:
    ival = -1

if ival > 0:
    print('Great choice')
else:
    print('Not a number')
