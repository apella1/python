# python comments 

''' 
This is a multiline comment also known as docstring (used to define a function's purpose )

'''


""" 
This is also a multiline comment. Both single and double line quotes can be used for that. 
Variable naming rules apply. 
Variable names can start with a letter or an underscore and not with a number
Variable names are case sensitive 

"""

# no semicolons or declaration keywords for python 

x = 4  #int 
y = 5.7 #float 
name = 'Robert Greene'   # strings can have either double or single quotes 
is_cool = True  # python boolean values start with a capital letter as opposed to javascript, java and php 

x = 8 # reassigning a variable 
# multiple assignments 

v, t, full_name, has_completed = (7, 8, 'Peter Gregory', False)


print(full_name, x, y, v, t, name)

# basic arithmetic operations can be assigned to a variable and displayed using the print function 

number_sum = 7 + 9

print(number_sum)

# checking the type of a variable - using type

# type casting
x = str(x)

print(type(y), y)

print(type(x))

y = int(y)

print(type(y), y)

z = float(y)

print(type(z), z)

# Few keywords to take note of 
# variable declaration - defining the variable 
# initialization - using the equal sign (=) to assign a value to a variable 
# initial value - it is advised to give an initial value to the variable however it isn't mandatory 


# * DATA TYPES 
# int, float, complex(for numbers besides int and float), bool, str
# more advanced data types - list, tuple, set, dict (dictionary)
# python allows the creation of custom data types using classes
# special data types - packages and modules - when the data definitions using the other data types aren't sufficient 
# None - similar to null in js - used to declare the absence of a value 


# * ARITHMETIC OPERATORS 
# +, -, *, **(exponential), /, %

print(2 ** 2)

# * Math functions on Int and Float data types 
# round() - rounds a float number to the nearest integer number 
# abs() - returns the absolute value of an argument 
# operator precedence - same for all programming languages  


# * CONSTANTS 
# using all caps and and underscore for compound names

PI = 3.14
EARTH_GRAVITY = 9.765

print(PI, EARTH_GRAVITY)


# Dunder Variables and Dunder Methods - double underscore - we should not try to change, modify or reassign such variables 

# Expressions - sequence of operators and operands that will produce a value 
# difference between expressions and statements 


# Augmented assignment operators +=, -=, *=, /=, //=(floor division and assignment), **=, %=

k = 6
j = 9

k += j # k = k + j

print(k)