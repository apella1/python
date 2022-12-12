# figuring how to read files within the same folder
try:
    fhand = open('files.txt')
    print(fhand)
    count = 0
    for line in fhand:
        count = count + 1
        if line.startswith('This'):
            line = line.rstrip() # removing whitespace by \n
            print(line)
    
    for ln in fhand:
        ln = ln.rstrip()
        if not ln.startswith('This'):
            continue
        print(ln)
    print('Line count:', count)

    # reading 
    file_data = fhand.read()
    print(len(file_data))
    print(file_data[:10])
except:
    print(1)


# the new line character - escaping
# /n is a character

word = 'Main\nStreet'
print(word, len(word))