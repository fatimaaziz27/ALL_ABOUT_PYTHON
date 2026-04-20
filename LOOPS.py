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

# Q) Keep looping until internet connection = True. 

while True:
    checking_connection=(input("do you have internet connection?  "))
    if checking_connection=="true":
        print("you are connected")
    if checking_connection=="false":
        print("check your connection")
        break

# OUTPUT:
# do you have internet connection?  tghfgh
# do you have internet connection?  true
# you are connected
# do you have internet connection?  true
# you are connected
# do you have internet connection?  false
# check your connection

# Q) While loop for chatbot (keep asking until user types “bye”). 

while True:
    chat=(input("do you have any question?  "))
    if chat=="bye":
        break

# OUTPUT:
# do you have any question?  some question
# do you have any question?  2 question
# do you have any question?  3 question
# do you have any question?  Bye 

# Q) Print seating chart for bus (Rows 1–3, Seats A–D).

rows= range(1, 4)
seats = ['A', 'B','C','D']
for row in rows:
    for seat in seats:
        print(f"{row}{seat}")

# OUTPUT:
# 1A
# 1B
# 1C
# 1D
# 2A
# 2B
# 2C
# 2D
# 3A
# 3B
# 3C
# 3D

# Q) Nested loop to find all team pairs from player list. 

players = ['Player1', 'Player2', 'Player3', 'Player4']
for i in range(len(players)):
    for j in range(i + 1, len(players)):
        print(f"Team: {players[i]} vs {players[j]}")

# OUTPUT:
# Team: Player1 vs Player2
# Team: Player1 vs Player3
# Team: Player1 vs Player4
# Team: Player2 vs Player3
# Team: Player2 vs Player4
# Team: Player3 vs Player4

# Q) Generate full multiplication tables from 2–5. 

# CODE:

i=2
while i <= 5:
    print(f"TABLE OF {i}")
    j=1
    while j<=10:
        print(f"{i} x {j} = {i*j}")
        j+=1
    print()
    i+=1    

# OUTPUT:

# TABLE OF 2
# 2 x 1 = 2
# 2 x 2 = 4
# 2 x 3 = 6
# 2 x 4 = 8
# 2 x 5 = 10
# 2 x 6 = 12
# 2 x 7 = 14
# 2 x 8 = 16
# 2 x 9 = 18
# 2 x 10 = 20

# TABLE OF 3
# 3 x 1 = 3
# 3 x 2 = 6
# 3 x 3 = 9
# 3 x 4 = 12
# 3 x 5 = 15
# 3 x 6 = 18
# 3 x 7 = 21
# 3 x 8 = 24
# 3 x 9 = 27
# 3 x 10 = 30

# TABLE OF 4
# 4 x 1 = 4
# 4 x 2 = 8
# 4 x 3 = 12
# 4 x 4 = 16
# 4 x 5 = 20
# 4 x 6 = 24
# 4 x 7 = 28
# 4 x 8 = 32
# 4 x 9 = 36
# 4 x 10 = 40

# TABLE OF 5
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# 5 x 4 = 20
# 5 x 5 = 25
# 5 x 6 = 30
# 5 x 7 = 35
# 5 x 8 = 40
# 5 x 9 = 45
# 5 x 10 = 50

# 58. How to break out of multiple nested loops in Python?

# Method 1: Using exceptions
try:
    for i in range(3):
        for j in range(3):
            for k in range(3):
                print(f"i: {i}, j: {j}, k: {k}")
                if i == 1 and j == 1 and k == 1:
                    raise StopIteration
except StopIteration:
    print("Loop broken")

# Method 2: Using flags
break_loop = False
for i in range(3):
    for j in range(3):
        for k in range(3):
            print(f"i: {i}, j: {j}, k: {k}")
            if i == 1 and j == 1 and k == 1:
                break_loop = True
                break
        if break_loop:
            break
    if break_loop:
        break

# Method 3: Using a function and return
def loop():
    for i in range(3):
        for j in range(3):
            for k in range(3):
                print(f"i: {i}, j: {j}, k: {k}")
                if i == 1 and j == 1 and k == 1:
                    return
loop()

# OUTPUT:
# i: 0, j: 0, k: 0
# i: 0, j: 0, k: 1
# i: 0, j: 0, k: 2
# i: 0, j: 1, k: 0
# i: 0, j: 1, k: 1
# i: 0, j: 1, k: 2
# i: 0, j: 2, k: 0
# i: 0, j: 2, k: 1
# i: 0, j: 2, k: 2
# i: 1, j: 0, k: 0
# i: 1, j: 0, k: 1
# i: 1, j: 0, k: 2
# i: 1, j: 1, k: 0
# i: 1, j: 1, k: 1
# Loop broken
# i: 0, j: 0, k: 0
# i: 0, j: 0, k: 1
# i: 0, j: 0, k: 2
# i: 0, j: 1, k: 0
# i: 0, j: 1, k: 1
# i: 0, j: 1, k: 2
# i: 0, j: 2, k: 0
# i: 0, j: 2, k: 1
# i: 0, j: 2, k: 2
# i: 1, j: 0, k: 0
# i: 1, j: 0, k: 1
# i: 1, j: 0, k: 2
# i: 1, j: 1, k: 0
# i: 1, j: 1, k: 1
# i: 0, j: 0, k: 0
# i: 0, j: 0, k: 1
# i: 0, j: 0, k: 2
# i: 0, j: 1, k: 0
# i: 0, j: 1, k: 1
# i: 0, j: 1, k: 2
# i: 0, j: 2, k: 0
# i: 0, j: 2, k: 1
# i: 0, j: 2, k: 2
# i: 1, j: 0, k: 0
# i: 1, j: 0, k: 1
# i: 1, j: 0, k: 2
# i: 1, j: 1, k: 0
# i: 1, j: 1, k: 1
