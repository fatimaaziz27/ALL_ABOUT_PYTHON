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

# Q) Loop through an email list and print only those ending with `@gmail.com`. 

emails = ["ME@example.com","123@gmail.com","MINE@yahoo.com","GHJ@gmail.com","NONE@hotmail.com"]
for email in emails:
    if email[-10:] == "@gmail.com":
        print(email)

# OUTPUT:
# 123@gmail.com
# GHJ@gmail.com

# Q) Print all words from a sentence in reverse order.

sentence = "SENTENCE THIS SPLIT I"
words = sentence.split()
words.reverse()
for word in words:
    print(word)

# OUTPUT:
# I
# SPLIT
# THIS
# SENTENCE

# Q) Keep asking user for password until it matches `"secure123"`. 

password = input("Enter password: ")
while password != "secure123":
    print("Incorrect password. Try again.")
    password = input("Enter password: ")
print("Password correct. Access granted.")

# OUTPUT:
# Enter password: yhdh
# Incorrect password. Try again.
# Enter password: secure123
# Password correct. Access granted.

# Q) ATM PIN check with max 3 attempts. 

pin = "123"
attempts = 0
while attempts < 3:
    user_pin = input("Enter 3-digit PIN: ")
    if len(user_pin) != 3 or not user_pin.isdigit():
        print("The PIN should contain exactly 3 digits.")
    elif user_pin == pin:
        print("PIN correct. Access granted.")
        break
        attempts += 1
else:
    print("Maximum attempts exceeded. Account locked.")

# OUTPUT:
# Enter PIN: fff
# Incorrect PIN. 2 attempts left.
# Enter PIN: ggg
# Incorrect PIN. 1 attempts left.
# Enter PIN: 123
# Access granted.

# Q) While loop to collect student marks until “done” entered. 

student_marks=[]
student_name=[]
while True:
    marks=(input("enter student marks: "))
    if marks =="done":
        break
    student_marks.append(marks)
    names=(input("enter student name: "))
    student_name.append(names)
print(student_marks)
print(student_name)

# OUTPUT:
# enter student marks: 97
# enter student name: yusra
# enter student marks: 79
# enter student name: asfiya
# enter student marks: 94
# enter student name: zainab
# enter student marks: done
# ['97', '79', '94']
# ['yusra', 'asfiya', 'zainab']
