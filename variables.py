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
