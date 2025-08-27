# Best practice questions:

# Q) Loop through an email list and print only those ending with `@gmail.com`. 

# CODE:

emails = ["ME@example.com","123@gmail.com","MINE@yahoo.com","GHJ@gmail.com","NONE@hotmail.com"]
for email in emails:
    if email[-10:] == "@gmail.com":
        print(email)

# OUTPUT:

# 123@gmail.com
# GHJ@gmail.com

# Q) Print all words from a sentence in reverse order.

# CODE:

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

# CODE:

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

# CODE:

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

# CODE:

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

# CODE:

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

# CODE:

while True:
    chat=(input("do you have any question?  "))
    if chat=="bye":
        break

# OUTPUT:

# do you have any question?  some question
# do you have any question?  2 question
# do you have any question?  3 question
# do you have any question?  Bye 

#Q) Print seating chart for bus (Rows 1–3, Seats A–D).

#CODE:

rows= range(1, 4)
seats = ['A', 'B','C','D']
for row in rows:
    for seat in seats:
        print(f"{row}{seat}")

#OUTPUT:

#1A
#1B
#1C
#1D
#2A
#2B
#2C
#2D
#3A
#3B
#3C
#3D

#Q) Nested loop to find all team pairs from player list. 

#CODE:

players = ['Player1', 'Player2', 'Player3', 'Player4']
for i in range(len(players)):
    for j in range(i + 1, len(players)):
        print(f"Team: {players[i]} vs {players[j]}")

#OUTPUT:

#Team: Player1 vs Player2
#Team: Player1 vs Player3
#Team: Player1 vs Player4
#Team: Player2 vs Player3
#Team: Player2 vs Player4
#Team: Player3 vs Player4

#Q) Generate full multiplication tables from 2–5. 

#CODE:

i=2
while i <= 5:
    print(f"TABLE OF {i}")
    j=1
    while j<=10:
        print(f"{i} x {j} = {i*j}")
        j+=1
    print()
    i+=1    

#OUTPUT:

#TABLE OF 2
#2 x 1 = 2
#2 x 2 = 4
#2 x 3 = 6
#2 x 4 = 8
#2 x 5 = 10
#2 x 6 = 12
#2 x 7 = 14
#2 x 8 = 16
#2 x 9 = 18
#2 x 10 = 20

#TABLE OF 3
#3 x 1 = 3
#3 x 2 = 6
#3 x 3 = 9
#3 x 4 = 12
#3 x 5 = 15
#3 x 6 = 18
#3 x 7 = 21
#3 x 8 = 24
#3 x 9 = 27
#3 x 10 = 30

#TABLE OF 4
#4 x 1 = 4
#4 x 2 = 8
#4 x 3 = 12
#4 x 4 = 16
#4 x 5 = 20
#4 x 6 = 24
#4 x 7 = 28
#4 x 8 = 32
#4 x 9 = 36
#4 x 10 = 40

#TABLE OF 5
#5 x 1 = 5
#5 x 2 = 10
#5 x 3 = 15
#5 x 4 = 20
#5 x 5 = 25
#5 x 6 = 30
#5 x 7 = 35
#5 x 8 = 40
#5 x 9 = 45
#5 x 10 = 50

#Q) Function to count how many `.pdf` files are in a list. 

#CODE:

files = ['file1.pdf', 'file2.txt', 'file3.pdf', 'file4.docx','file5.pdf','file6.pdf']
def pdf__count():
    count = len([file for file in files if file.endswith('.pdf')])
    print(count)
pdf__count()

#OUTPUT:  4

