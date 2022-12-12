# using reserved list class

my_array = list()
my_array.append('Good Morning')
my_array.append('Bonsour')
print(my_array)


# 'in' operator

print('Hello' in my_array)
print('Hello' not in my_array)


# sorting
my_array.sort()
print(my_array)


# built-in functions

nums = [3, 1, 8, 9]
min_nums = min(nums)
max_nums = max(nums)
sum_nums = sum(nums)
average_nums = sum_nums / len(nums)

print(min_nums, max_nums, sum_nums, average_nums)