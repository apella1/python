import random

age = 4
my_list = [2, 5, 6, 7]
name = "John"
color = "red"

# concatenating string and numbers
print("My name is " + name + " and I am " + str(age) + " years old.")
print(f'My name is {name} and I am {age} years old.')

#  program to automate tasks

# add two numbers with user input

print(random.randint(0, 9))

# checking prime number
num = 30

flag = False

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break

if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")
