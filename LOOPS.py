#                 LOOPS:

# Q) What will be the output of the following code?

def power(base, exponent=2):
    return base ** exponent

print(power(3))
print(power(2, 3))

# OUTPUT:
# 9
# 8


def multiply(a, b):
    return a * b

def square(num):
    return multiply(num, num)

print(square(3))

Output:

9

Explanation:

square(3) → multiply(3, 3) → 3 × 3 = 9

✅ Q3
def sum_numbers(*args):
    return sum(args)

print(sum_numbers(1, 2, 3, 4, 5))

Output:

15

Explanation:

Adds all numbers → 1+2+3+4+5 = 15

✅ Q4
def reverse_list(lst):
    return lst[::-1]

print(reverse_list([1, 2, 3, 4, 5]))

Output:

[5, 4, 3, 2, 1]

Explanation:

[::-1] reverses the list

✅ Q5
def count_evens(lst):
    count = 0
    for num in lst:
        if num % 2 == 0:
            count += 1
    return count

print(count_evens([1, 2, 3, 4, 5, 6]))

Output:

3

Explanation:

Even numbers: 2, 4, 6 → total = 3

✅ Q6
def find_key_by_value(d, value):
    for key, val in d.items():
        if val == value:
            return key
    return "Not found"

print(find_key_by_value({"x": 10, "y": 20, "z": 30}, 20))

Output:

y

Explanation:

Value 20 belongs to key "y"

✅ Q7
def greet(name):
    def message():
        return f"Hello, {name}!"
    return message()

print(greet("Alice"))

Output:

Hello, Alice!

Explanation:

Inner function returns greeting with name