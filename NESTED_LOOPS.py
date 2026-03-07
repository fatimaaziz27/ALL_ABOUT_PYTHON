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

# 1 x 1 = 1

# 1 x 2 = 2

# 1 x 3 = 3

# 1 x 4 = 4

# 1 x 5 = 5

# 2 x 1 = 2

# 2 x 2 = 4

# 2 x 3 = 6

# 2 x 4 = 8

# 2 x 5 = 10

# 3 x 1 = 3

# 3 x 2 = 6

# 3 x 3 = 9

# 3 x 4 = 12

# 3 x 5 = 15

# Q) What will be the output of the following code?

names = [["aina","yusra"],["samiya","amna"]]
for group in names:
    for name in group:
        print(name)

# OUTPUT: