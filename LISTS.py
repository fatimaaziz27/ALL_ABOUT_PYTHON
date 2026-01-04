#                                         lists:

# Q) What will be the output of the following code?
my_list = [1, 2, 3, 4, 5]
print(my_list[2])
# OUTPUT:
# 3
# Q) What will be the output of the following code?
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)
# OUTPUT:
# ['apple', 'banana', 'cherry', 'orange']

# Q) What will be the output of the following code?
numbers = [10, 20, 30, 40, 50]
numbers.remove(30)
print(numbers)
# OUTPUT:
# [10, 20, 40, 50]
# Q) What will be the output of the following code?
colors = ["red", "green", "blue"]
print(len(colors))
# OUTPUT:
# 3
# Q) What will be the output of the following code?
mixed_list = [1, "two", 3.0, True]
print(type(mixed_list[1]))
# OUTPUT:
# <class 'str'>
# Q) What will be the output of the following code?
my_list = [5, 10, 15, 20]
my_list[1] = 25
print(my_list)
# OUTPUT:
# [5, 25, 15, 20]
# Q) What will be the output of the following code?
numbers = [1, 2, 3, 4, 5]
squared_numbers = [x**2 for x in numbers]
print(squared_numbers)
# OUTPUT:
# [1, 4, 9, 16, 25]
# Q) What will be the output of the following code?
a = [1, 2, 3]
b = a
b.append(4)
print(a)
# OUTPUT:
# [1, 2, 3, 4]
# Q) What will be the output of the following code?