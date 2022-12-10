# slicing - upto but not including the second parameter

word = 'Respect is not given, it is earned.'

word_slice = word[5:7]

print(word_slice)
print(word[:6], word[0:], word[:], word[:len(word) - 1])


# 'in' as a logical operator

print('monty' in word, 'is' in word)


# string library

lower_word = word.lower()
upper_word = word.upper()
capital_word = word.capitalize()

print(lower_word)
print(upper_word)
print(capital_word)
print('hello'.upper())
print('nice'.capitalize())
print(type(word))
print(dir(word))  # methods available for strings