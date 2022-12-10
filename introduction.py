"""

Interpreted, object oriented, high level with dynamic semantics
general language - used to solve different problems
- websites, software, data analysis, ML, AI
Created by Guido van Rossum and was first released on Feb 20th, 1991
Python interpreter is written and implemented as as a C program
hence the VM's name CPython

"""

string = '123'

print(string + '1')

new_string = input('Enter first name: ')

print(f'Your first name is {new_string}')

print(f'This is an f string')

def greet(lang, name):
    if lang == 'es':
        print(f'Hola, {name}')
    elif lang == 'eng':
        print(f'Hello, {name}')
    elif lang == 'fr':
        print(f'Bonsour, {name}')
    else:
        new_lang = input('Which language do you speak? ')
        print(f'We are working to include {new_lang} in our language servers.')


greet('fr', 'Griezmann')
