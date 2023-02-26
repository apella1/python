# python comments

'''
Multiline comment aka docstring (used to define a function's purpose )

'''


"""
This is also a multiline comment. Single and double quotes alike.
Variable naming rules apply
Variable names can start with a letter or an underscore and not with a number
Variable names are case sensitive

"""

# no semicolons or declaration keywords for python

x = 4  # int
y = 5.7 # float
name = 'Robert Greene'   # strings can have either double or single quotes

 # python booleans start with a capital as opposed to javascript, java and php
is_cool = True

x = 8 # reassigning a variable

# multiple assignments

v, t, full_name, has_completed = (7, 8, 'Peter Gregory', False)


print(full_name, x, y, v, t, name)

# assignment statements for variable declarations

number_sum = 7 + 9

print(number_sum)
print(type(number_sum))

# checking the type of a variable - using type()

# type casting
x = str(x)

print(type(y), y)

print(type(x))

y = int(y)

print(type(y), y)

z = float(y)

print(type(z), z)

item_price = 60
p = float(item_price)

print(p, type(p))

# Few keywords to take note of
# variable declaration
# initialization - using (=) to assign a value to a variable
# it is advised to give an initial value to the variable


# * DATA TYPES
# int, float, complex(for numbers besides int and float), bool, str
# more advanced data types - list, tuple, set, dict (dictionary)
# python allows the creation of custom data types using classes
# special data types - packages and modules
# None - similar to null in js - used to declare the absence of a value


# * ARITHMETIC OPERATORS
# +, -, *, **, /, %

print(2 ** 2)

# * Math functions on Int and Float data types
# round() - rounds a float number to the nearest integer number
# abs() - returns the absolute value of an argument
# operator precedence - same for all programming languages


# * CONSTANTS
# using all caps and and underscore for compound names

PI = 3.14

EARTH_GRAVITY = 9.765

VISCOSITY = 99

print(PI, EARTH_GRAVITY, VISCOSITY)

# Dunder Variables and Dunder Methods - double underscore
# shouldn't be changed, modified or reassigned

# Expressions - sequence of operators and operands that will produce a value
# difference between expressions and statements


# Augmented assignment operators +=, -=, *=, /=, //=(floor division), **=, %=

k = 6
j = 9

k += j # k = k + j

print(k)

