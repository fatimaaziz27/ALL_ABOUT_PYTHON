# Q) What will be the output of the following code?

def is_even(num):
    return num%2==0
print(is_even(4))

# OUTPUT:
# True

# Q) What will be the output of the following code?

def reverse_string(s):
    return s[::-1]
print(reverse_string("hello"))

# OUTPUT:
# olleh

# Q) What will be the output of the following code?

def square(n):
    return n*n
print(square(3))

# OUTPUT:
# 9

# Q) What will be the output of the following code?

def convert_temperature(value,scale="c"):
    if scale == "c":
        return (value * 9/5) + 32     # convert to fahrenheit
    else:
        return (value - 32) * 5/9      # convert to celsius

print(convert_temperature(0,"c"))

# OUTPUT:
# 32.0