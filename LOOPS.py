6#                 LOOPS:
Q1
for i in range(1, 6):
    print(i)

Output:
1
2
3
4
5

Q2
for i in range(2, 11, 2):
    print(i)

Output:
2
4
6
8
10

Q4
num = 5
while num > 0:
    print(num)
    num -= 1

Output:
5
4
3
2
1

Q5
total = 0
for i in range(1, 11):
    total += i
print(total)

Output:
55

Q6
for i in range(1, 10):
    if i == 5:
        break
    print(i)

Output:
1
2
3
4

Q7
for i in range(1, 6):
    if i % 2 == 0:
        continue
    print(i)

Output:
1
3
5

Q8
numbers = [5, 9, 2, 8, 1]
max_num = numbers[0]

for num in numbers:
    if num > max_num:
        max_num = num

print(max_num)

Output:
9