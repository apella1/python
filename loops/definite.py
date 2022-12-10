# for loop

numbers = [11, 44, 5, 9]

for i in numbers:
    print(i)
print('Loop done!')

cars = ['Chevy', 'Benz', 'Audi', 'BMW']

for car in cars:
    print(f'This {car} is amazing!')


# * Finding the largest number in numbers

largest = None

for number in numbers:
    if largest is None:
       largest = number
    elif number > largest:
        largest = number
    print(largest, number)
print('The largest number in the list is', largest) 


# Finding the smallest number in numbers

smallest = None

for number in numbers:
    if smallest is None:
        smallest = number
    elif number < smallest:
        smallest = number
    print(smallest, number)
print('The smallest number is', smallest)

# counting in numbers

count = 0
total = 0

for n in numbers:
    count = count + 1
    print(count, n)
    total = total + n
    average = total / count
print('Sum', total)
print('Average', average)


# filtering in a loop

for n in numbers:
    if n < 10:
        print('Small number', n)


# Searching using a boolean
names = ['Pete', 'Gray', 'Dave', 'Glad']

foundName = False

for name in names:
    if name == 'Dave':
        foundName = True
        print(foundName, name)
        break
    print(foundName, name)