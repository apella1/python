# lists are similar to arrays in js
# lists - data structure
# data structures allow us to store data in an organized container

odd_numbers = [1, 3, 5, 7, 9]

letters = ['a', 'b', 'c', 'd']

number_letters = [1, 6, 'h', 'g', 7]

print(odd_numbers)
print(letters)
print(number_letters[0])

print(type(odd_numbers), type(letters), type(number_letters))

print(len(letters))


#  list slicing - sliced elements can be stored in a variable
# original list is not affected
# how does this compare to javascript slice and splice array methods?

print(letters[0:4])
print(number_letters[2:3])
print(odd_numbers[3:4])

# we can also include the step size of the lists if we so desire

even_numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]

print(even_numbers[2::4])

# lists are mutable i.e we can change the elements of a list after the list has been created
# strings are similar to lists in a lot of ways except strings are immutable (the characters cannot be changed once declared)

# changing the elements of a list
number_letters[0] = 'c'

print(number_letters)
