# taking user inputs and computing operations 

first_number = input('Enter the first number: ')
second_number = input('Enter the second number: ')
number_sum = int(first_number) + int(second_number) # explicit type conversion 

print(type(first_number), type(second_number))
print(f'The sum of the two numbers is {number_sum}')