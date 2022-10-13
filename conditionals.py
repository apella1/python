# works pretty much the same way just as in other programming languages 

num1 = 5
num2 = 5
number_sum = num1 + num2 
number_difference = abs(num1 - num2)
difference = num1 - num2

if number_sum > 10:
    print(f'{number_sum} is greater than 10.')
elif number_sum == 10:
    print(f'The sum of the two numbers is {number_sum}')
else:
    print(f'{number_sum} is less than 10.')

# using logical operators (and, or, not) - instead of nesting if statements within if statements 
print(number_difference)

print(difference)

if number_difference > 0 and number_sum / 2 != num1:
    print(f'{num1} is not equal to {num2}')
elif number_difference == 0 or number_sum / 2 == num1 or num2:
    print(f'{num1} is equal to {num2}')

# membership operators (not, not in)
x = 5
y = 5
numbers = [1, 2, 3, 4, 5]

if x in numbers:
    print(x in numbers) # prints true or false 
elif x not in numbers:
    print(x not in numbers)

# identity operators (is and is not) - is not works opposite to is 

if x is y:
    print(x is y)
else:
    print(f'{x} is not equal to {y}')