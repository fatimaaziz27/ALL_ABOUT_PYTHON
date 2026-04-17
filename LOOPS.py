#                 LOOPS:

# Q) What will be the output of the following code?

for i in range(1, 6):
    print(i)

# Output:
# 1
# 2
# 3
# 4
# 5

# Q) What will be the output of the following code?

for i in range(2, 11, 2):
    print(i)

# Output:
# 2
# 4
# 6
# 8
# 10

# Q) What will be the output of the following code?

num = 5
while num > 0:
    print(num)
    num -= 1

# Output:
# 5
# 4
# 3
# 2
# 1

# Q) What will be the output of the following code?

total = 0
for i in range(1, 11):
    total += i
print(total)

# Output:
# 55

# Q) What will be the output of the following code?

for i in range(1, 10):
    if i == 5:
        break
    print(i)

# Output:
# 1
# 2
# 3
# 4

# Q) What will be the output of the following code?

for i in range(1, 6):
    if i % 2 == 0:
        continue
    print(i)

# Output:
# 1
# 3
# 5

# Q) What will be the output of the following code?

numbers = [5, 9, 2, 8, 1]
max_num = numbers[0]

for num in numbers:
    if num > max_num:
        max_num = num

print(max_num)

# Output:
# 9

# Q) What will be the output of the following code?

t = (1, 2, 3, 2, 2, 4, 5)
count = 0

for num in t:
    if num == 2:
        count += 1

print(count)

# Output:
# 3

# Q) What will be the output of the following code?

person = {"name": "Alice", "age": 25, "city": "New York"}

for key in person:
    print(key)

# Output:
# name
# age
# city

# Q) What will be the output of the following code?

student = {"name": "Bob", "grade": "A", "subject": "Math"}

for value in student.values():
    print(value)

# Output:
# Bob
# A
# Math

# Q) What will be the output of the following code?

car = {"brand": "Toyota", "model": "Camry", "year": 2022}
key_to_find = "year"
found = False

for key in car:
    if key == key_to_find:
        found = True
        break

print(found)

# Output:
# True