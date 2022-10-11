# ? what differentiates functions and methods 

'''

Built in functions - ends with the double brackets 
abs, alter, all, any, anext, ascii, bin, bool, breakpoint, bytearray, bytes, callable, chr, classmethod, compile, complex
delattr, dict, dir, divmod, enumerate, eval, exec, filter, float, format, frozenset, getattr, globals, hasattr, hash, help, hex
id, input, int, isinstance, issubclass, iter, len, list, locals, map, max, memoryview, min, next
object, oct, open, ord, pow, print, property, range, rpr, reversed, round, set, setattr, slice, sorted, staticmethod, str, sum, super, tuple, type, vars, zip
_import_ 

'''


# useful built-in functions 
text = 'This is an amazing script'

print(len(text))

upper_text = text.upper() # lower works the same way in reverse

print(upper_text)

print('how has your day been?'.capitalize()) # capitalize turns the first letter into a capital letter

print(text.find('day')) # finding the first occurrence of the specified string

print(text.replace('script', 'program'))

join_string = '-'.join(['Python', 'is', 'awesome'])
print(join_string.lower())
