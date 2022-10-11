# string formatting and string methods 

name = 'Carl Jung'
age = 66

print('Hello, my name is ' + name + '.') #concatenation 

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
first_name = 'Freddie'
last_name = 'Roach'

print(f'{first_name} {last_name} is an amazing coach.')

# string indices 
print(first_name[3]) 


