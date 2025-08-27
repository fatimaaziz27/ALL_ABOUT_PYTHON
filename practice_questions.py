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
