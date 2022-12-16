# for loop - iterating over a sequence i.e lists, tuples, dictionaries, sets

names = ['Many', 'Joseph', 'Carter', 'Rockefeller', 'Greene']

# similar to for (let name of names) {} in javascript
for name in names:
    print(f'Current name: {name}')


# breaking out of a loop
for person in names:
    if person == 'Carter':
        break
print(f'Current person: {person}')


n = 10

while n > 0:
    print(n)
    n = n - 1
print('Done looping')
print(n)

number = 10
total = 0

while number > 0:
    print(number)
    total += number
    number -= 1
print(total)