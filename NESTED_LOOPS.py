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
# aina
# yusra
# samiya
# amna

# Q) What will be the output of the following code?

words = ["hi","hello","world"]
vowels = "aeiou"
for word in words:
    count = 0
    for char in word:
        if char in vowels:
            count += 1
            print(f"{word}:{count}")

# OUTPUT:
# hi:1
# hello:1
# hello:2
# world:1

# Q) What will be the output of the following code?

i = 1
while i <= 3:
    j=1
    while j<=5:
        print(f"{i} x {j} = {i*j}")
        j += 1
        print()
        i += 1


# OUTPUT:
# 1x1=1

# 2x2=4

# 3x3=9

# 4x4=16

# 5x5=25