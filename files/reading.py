fName = input('Enter file name: ')

try:
    fHand = open(fName)
except:
    print(f'File {fName} does not exist')
    quit()

count = 0

for line in fHand:
    count = count + 1
    line = line.rstrip()
print(f'There are {count} number of lines in {fHame}')

# reading the file data

file_data = fHand.read()
print(len(file_data))