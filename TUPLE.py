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

