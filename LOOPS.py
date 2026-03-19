#                 LOOPS:

# Q) What will be the output of the following code?

def power(base, exponent=2):
    return base ** exponent

print(power(3))
print(power(2, 3))

# OUTPUT:
# 9
# 8

# Q) What will be the output of the following code?

def multiply(a, b):
    return a * b

def square(num):
    return multiply(num, num)

print(square(3))

# OUTPUT:
# 9

# Q) What will be the output of the following code?

def sum_numbers(*args):
    return sum(args)

print(sum_numbers(1, 2, 3, 4, 5))

# OUTPUT:
# 15

# Q) What will be the output of the following code?

def reverse_list(lst):
    return lst[::-1]

print(reverse_list([1, 2, 3, 4, 5]))

# OUTPUT:
# [5, 4, 3, 2, 1]

# Q) What will be the output of the following code?

def count_evens(lst):
    count = 0
    for num in lst:
        if num % 2 == 0:
            count += 1
    return count

print(count_evens([1, 2, 3, 4, 5, 6]))

# OUTPUT:
# 3

# Q) What will be the output of the following code?

def find_key_by_value(d, value):
    for key, val in d.items():
        if val == value:
            return key
    return "Not found"

print(find_key_by_value({"x": 10, "y": 20, "z": 30}, 20))

Output:

y

# Q) What will be the output of the following code?

def greet(name):
    def message():
        return f"Hello, {name}!"
    return message()

print(greet("Alice"))

Output:
Hello, Alice!
