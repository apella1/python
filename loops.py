# for loop - iterating over a sequence i.e lists, tuples, dictionaries, sets, strings

names = ['Manny', 'Joseph', 'Carter', 'Rockefeller', 'Greene']

# similar to for (let name of names) {} in javascript 
for name in names:
    print(f'Current name: {name}')


# breaking out of a loop 
for person in names:
    if person == 'Joseph':
        break
print(f'Current person: {person}')
