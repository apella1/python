# string formatting and string methods 

name = 'Carl Jung'
age = 66


print(len(name))
print(name[7])
print('Hello, my name is ' + name + '.') #concatenation 
print(f'Pleased to meet {name}')

# long strings stretching to multiple lines 

text = '''
first line
second line
third line
'''

print(text)


# Type casting - type conversion 

# implicit type conversion 

x = 7
y = 3.3
number_sum = x + y
number_quotient = x / y

print(number_sum, number_quotient) # yields 10.3 - conversion done to avoid data loss 


# escape sequence - same as in js
summary = 'I\'m excited to be at this meeting.'

print(summary)


# formatted strings 
first_name = 'Tony'
last_name = 'Kariohki'

print(f'{first_name} {last_name} is an amazing mentor.')

# string indices 
print(first_name[3]) 

# in keyword 
book_title = 'Hitchhiker\'s Guide to The Galaxy'

print('The' in book_title)


# Looping through strings

name = 'Prometheus'
index = 0

while index < len(name):
    letter = name[index]
    print(index, letter)
    index = index + 1


for ltr in name:
    print(ltr)


# finding the number of times a letter exists

myLetter = 'e'
letter_count = 0

for lett in name:
    if lett == myLetter:
        letter_count = letter_count + 1
print(letter_count)
