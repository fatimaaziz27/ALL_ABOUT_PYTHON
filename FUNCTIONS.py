#                 FUNCTIONS:

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

# OUTPUT:
# y

# Q) What will be the output of the following code?

def greet(name):
    def message():
        return f"Hello, {name}!"
    return message()

print(greet("Alice"))

# OUTPUT:
# Hello, Alice!

# Q) Find first non-repeated character in string. 

def first_non_repeated(s):
    for char in s:
        if s.count(char) == 1:
            return char
    return None
# Example usage:
s = "none"
print("First non-repeated character:", first_non_repeated(s))

# OUTPUT:
# First non-repeated character: o

# Q) A machine that takes user input for product name and tells the price of the product if it's available in the list.

products = {
    "Apple": 100,
    "Banana": 50,
    "Orange": 75,
    "Mango": 200,
    "Grapes": 150
}
def get_product_price(product_name):
    if product_name in products:
        return f"The price of {product_name} is {products[product_name]} PKR"
    else:
        return f"Sorry, {product_name} is not available or not for sale."
while True:
    product_name = input("Enter product name (or 'quit' to stop): ")
    if product_name.lower() == 'quit':
        break
    print(get_product_price(product_name.capitalize()))

# OUTPUT:
# Enter product name (or 'quit' to stop): apple
# The price of Apple is 100 PKR
# Enter product name (or 'quit' to stop): mango
# The price of Mango is 200 PKR
# Enter product name (or 'quit' to stop): peach
# Sorry, Peach is not available or not for sale.
# Enter product name (or 'quit' to stop): quit
