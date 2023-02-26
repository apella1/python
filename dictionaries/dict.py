purse = dict()

purse['Book'] = 1
purse['Money'] = 12
purse['Food'] = 3
purse['Money'] = 9

print(purse['Money'])
print(purse['Food'])
print(purse['Book'])
print(purse['Food'])

person = {
    'name': 'Carl Jay',
    'age': 7,
    'hobby': 'probably eating',
    'tall': False
}

"""Dictionaries are created as key-value pairs"""
items = {'Pragmatic': 1, 'Eloquent': 2, 'Microservices': 3, 'JavaScript': 4, 'Backend': 5, 'Dragon': 6}

print(items.values())
print(items.keys())
print(items.items())

books = {'study': 'Deep Work', 'health': 'Facets of Health', 'meaning': 'The 12 Rules of Life'}

print(books.items())
print(books.values())
print(books.keys())

# programming language dictionary

language = {
    'name': 'Java',
    'age': 53,
    'uses': ['web development', 'microservices', 'android development'],
    'creator': 'James Gosling'
}

print(language)