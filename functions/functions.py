# ? what differentiates functions and methods
# methods are functions within functions

'''

Built in functions - ends with the double brackets

object, oct, open, ord, pow, print, property, range, rpr, reversed, bytearray,
bytes, callable, chr, classmethod, compile, complex
dir, id, input, int, isinstance, issubclass, iter, len, list, locals, map,
max, memoryview, min, next
divmod, enumerate, eval, exec, filter, float, format, frozenset, getattr,
globals, hasattr, hash, help, hex
abs, alter, all, any, anext, ascii, bin, bool, breakpoint, delattr, dict,
round, set, setattr, slice, sorted, staticmethod,
str, sum, super, tuple, type, vars, zip

_import_

'''


# useful built-in functions

text = 'This is an amazing script'

print(len(text))

# lower works the same way in reverse
upper_text = text.upper()

print(upper_text)

# capitalize turns the first letter into a capital letter
print('how has your day been?'.capitalize())

# finding the first occurrence of the specified string
print(text.find('day'))
print(text.replace('script', 'program'))

join_string = '-'.join(['Python', 'is', 'awesome'])
print(join_string.lower())

# a function is executed only when it's called

def sayHello(name, age):
    print(f'{name} is {age} years old')


sayHello('Paul Graham', 45)

# setting defaults for functions
def jobSummary(position = 'doctor'):
    print(f'Being a {position} is great.')


jobSummary()

jobSummary('software developer')


# return values
# total is defined within the function's local scope

def getSum(num1, num2):
    total = num1 + num2
    return total


print(getSum(3, 5))


# lambda functions - similar to javascript's arrow functions

getProduct = lambda first_digit, second_digit: first_digit * second_digit

print(getProduct(4, 6))

big = max('This is a plantation')
print(big)