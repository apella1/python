age = 4
my_list = [2, 5, 6, 7]  
name = "John"
color = "blue"

print("My name is " + name + " and I am " + str(age) + " years old.")


#  program to automate tasks

# add two numbers with user input

import random 

print(random.randint(0, 9))

# checking prime number 
num = 11

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
