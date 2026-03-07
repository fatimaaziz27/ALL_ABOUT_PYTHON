#           NESTED LOOPS ------->

# Q) What will be the output of the following code?

for i in range(1,4):
    for j in range(1,4):
        print(i,j)

# OUTPUT:
# 1 1
# 1 2
# 1 3
# 2 1
# 2 2
# 2 3
# 3 1
# 3 2
# 3 3

# Q) What will be the output of the following code?

for i in range(1,4):
    for j in range(1,6):
        print(f"{i} x {j} = {i*j}")
        print()

# OUTPUT:
