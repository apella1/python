# concatenating lists

odd_numbers = [1, 3, 5]
even_numbers = [2, 4, 5]
all_numbers = odd_numbers + even_numbers
reverse_all = even_numbers + odd_numbers

print(all_numbers)
print(reverse_all)


# list slicing
# up to but not including the last value
# steps given by using double colon


print(odd_numbers[::2])


print(dir(odd_numbers))