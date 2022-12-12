fname = input('Enter file name: ')

try:
    fhand = open(fname)
except:
    print(f'File {fname} does not exist')
    quit()

count = 0

for line in fhand:
    count = count + 1
    line = line.rstrip()
print(f'There are {count} number of lines in {fname}')

# reading the file data

file_data = fhand.read()
print(len(file_data))