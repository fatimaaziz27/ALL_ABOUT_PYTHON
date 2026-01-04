#                                         lists:

# Q) What will be the output of the following code?

fruits = ["apple", "banana", "cherry"]
print(fruits[1])

# OUTPUT:
# banana

# Q) What will be the output of the following code?

numbers = [1, 2, 3, 4,]
numbers[2]=10
print(numbers)

# OUTPUT:
# [1, 2, 10, 4]

# Q) What will be the output of the following code?

colors = ["red", "blue"]
colors.append("green")
print(colors)

# OUTPUT:
# ['red', 'blue', 'green']

# Q) What will be the output of the following code?

nums = [10, 20, 30, 40, 50]
print(nums[1:4])

# OUTPUT:
# [20, 30, 40]

# Q) What will be the output of the following code?

names = ["Alice", "Bob", "Charlie"]
print("Alice" in names)

# OUTPUT:
# True

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

my_list = [10, 20, 30, 40, 50]
print(my_list[-1])

# OUTPUT:
# 50

# Q) What will be the output of the following code?

letters = ['a', 'b', 'c', 'd']
print(letters[1:3])

# OUTPUT:
# ['b', 'c']

# Q) What will be the output of the following code?

nums = [1, 2, 3, 4, 5]
nums.clear()
print(nums)

# OUTPUT:
# []

# Q) What will be the output of the following code?

my_list = [1, 2, 3, 4, 5]
print(sum(my_list))

# OUTPUT:
# 15

# Q) What will be the output of the following code?

items = ['pen', 'pencil', 'eraser']
items.insert(1, 'marker')
print(items)

# OUTPUT:
# ['pen', 'marker', 'pencil', 'eraser']

# Q) What will be the output of the following code?

numbers = [3, 1, 4, 1, 5]
numbers.sort()
print(numbers)

# OUTPUT:
# [1, 1, 3, 4, 5]

# Q) What will be the output of the following code?

a = [1, 2, 3]
b = [4, 5, 6]
combined = a + b
print(combined)

# OUTPUT:
# [1, 2, 3, 4, 5, 6]

# Q) What will be the output of the following code?

my_list = [10, 20, 30, 40, 50]
print(my_list.index(30))

# OUTPUT:
# 2

# Q) What will be the output of the following code?

fruits = ["apple", "banana", "cherry", "date"]
print("banana" in fruits)

# OUTPUT:
# True

# Q) What will be the output of the following code?

numbers = [1, 2, 3, 4, 5]
print(numbers.count(3))

# OUTPUT:
# 1

# Q) What will be the output of the following code?

my_list = [1, 2, 3, 4, 5]
reversed_list = my_list[::-1]
print(reversed_list)

# OUTPUT:
# [5, 4, 3, 2, 1]

# Q) What will be the output of the following code?

a = [1, 2, 3]
b = a.copy()
b.append(4)
print(a)

# OUTPUT:
# [1, 2, 3]

# Q) What will be the output of the following code?

numbers = [10, 20, 30, 40, 50]
del numbers[2]
print(numbers)

# OUTPUT:
# [10, 20, 40, 50]

# Q) What will be the output of the following code?

my_list = [1, 2, 3, 4, 5]
print(min(my_list))

# OUTPUT:
# 1

# Q) What will be the output of the following code?

values = [5, 10, 15, 20]
average = sum(values) / len(values)
print(average)

# OUTPUT:
# 12.5

# Q) What will be the output of the following code?

chars = ['a', 'b', 'c', 'd']
chars.pop()
print(chars)

# OUTPUT:
# ['a', 'b', 'c']

# Q) What will be the output of the following code?

my_list = [2, 4, 6, 8, 10]
even_numbers = [x for x in my_list if x % 2 == 0]
print(even_numbers)

# OUTPUT:
# [2, 4, 6, 8, 10]

# Q) What will be the output of the following code?

items = ['a', 'b', 'c', 'd']
items.extend(['e', 'f'])
print(items)

# OUTPUT:
# ['a', 'b', 'c', 'd', 'e', 'f']