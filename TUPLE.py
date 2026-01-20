# Q1) what will be the output of the following code?

my_tuple = (1, 2, 3, 4, 5)
if 3 in my_tuple:
    print("3 is present")
else:
    print("3 is missing")

# OUTPUT:
# 3 is present

# Q2) what will be the output of the following code?

t = (1,2,3)
t[1] = 10
print(t)

# OUTPUT:
# TypeError: 'tuple' object does not support item assignment

# Q3) what will be the output of the following code?

t = (5,)
print(type(t))

# OUTPUT:
# <class 'tuple'>

# Q4) what will be the output of the following code?

t = (1, 2, 3, 4, 5)
print(t[::2])

# OUTPUT:
# (1, 3, 5)

# Q5) what will be the output of the following code?

t1 = (1, 2, 3)
t2 = (4, 5, 6)
t3 = t1 + t2
print(t3)

# OUTPUT:
# (1, 2, 3, 4, 5, 6)

# Q6) what will be the output of the following code?

fruit = ("apple", "banana", "cherry")
print("banana" in fruit)

# OUTPUT:
# True

# Q7) what will be the output of the following code?

t = (1, 2, 3, 4, 5)
print(len(t))

# OUTPUT:
# 5

# Q7) What will be the output of the following code?

numbers = (10, 20, 30, 40, 50)
if 25 in numbers:
    print("25 is present")
else:
    print("25 is missing")

# OUTPUT:
# 25 is missing

# Q8) What will be the output of the following code?

value = (100, 200, 300)
if 200 in value:
    print("200 is present")
else:
    print("200 is missing")

# OUTPUT:
# 200 is present

# Q9) What will be the output of the following code?

data = (1, 2, 3, 4, 5)
if data[0] == 1:
    print("First element is 1")
else:
    print("First element is not 1")

# OUTPUT:
# First element is 1

# Q10) What will be the output of the following code?

info = ("Alice", 30, "Engineer")
if info[1] > 18:
    print("Adult")
else:
    print("Minor")

# OUTPUT:
# Adult

