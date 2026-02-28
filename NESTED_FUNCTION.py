# Q) What will be the output of the following code?

def math_operation(a,b):
    def add():
        return a + b
    return add()
print(math_operation(7,2))

# OUTPUT:
# 9