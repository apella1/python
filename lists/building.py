# using reserved list class

my_array = list()
my_array.append('Good Morning')
my_array.append('Bonsour')
print(my_array)

goods = list()
goods.append('Shoes')
goods.append('Watch')
goods.append('Apples')

print(goods[:1])

# 'in' operator

print('Good' in my_array)
print('Hello' not in my_array)
print('Books' in goods)


# sorting
my_array.sort()
print(my_array)

goods.sort()
print(goods)

# built-in functions

nums = [3, 1, 8, 9]
min_nums = min(nums)
max_nums = max(nums)
sum_nums = sum(nums)
average_nums = sum_nums / len(nums)

print(min_nums, max_nums, sum_nums, average_nums)

print(max(goods))