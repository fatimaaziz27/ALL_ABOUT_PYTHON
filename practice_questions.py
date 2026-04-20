# Best practice questions:

# Q) Function to count how many `.pdf` files are in a list. 

# CODE:

files = ['file1.pdf', 'file2.txt', 'file3.pdf', 'file4.docx','file5.pdf','file6.pdf']
def pdf__count():
    count = len([file for file in files if file.endswith('.pdf')])
    print(count)
pdf__count()

# OUTPUT:  4

"""
Basic inheritance?

Q) Create a class 'Animal' with a method 'speak()' that prints "Animal speaks".
Now create a subclass 'Dog' that inherits from 'Animal' and overrides the 'speak()' method to print "Dog barks".
Create objects of both classes and call the 'speak()' method.

"""
# ANSWER:

class Animal:
    def speak(self):
        """Prints a generic animal sound"""
        print("Animal speaks")
class Dog(Animal):
    def speak(self):
        """Overrides the speak method to print a dog's sound"""
        print("Dog barks")
animal = Animal()
dog = Dog()
animal.speak()  
dog.speak()

# OUTPUT:

# Animal speaks
# Dog barks

"""
Multi-Level Inheritance

Q) Create a class 'Vehicle', then create a subclass 'Car', and then a subclass 'ElectricCar' that inherits from 'Car'.
Each class should have one method that prints something specific to that class.
Create an object of 'ElectricCar' and call all methods from each level.

"""
# ANSWER:

class Vehicle:
    def vehicle_method(self):
        """Prints a message specific to Vehicle"""
        print("This is a vehicle.")
class Car(Vehicle):
    def car_method(self):
        """Prints a message specific to Car"""
        print("This is a car.")
class ElectricCar(Car):
    def electric_car_method(self):
        """Prints a message specific to ElectricCar"""
        print("This is an electric car.")
electric_car = ElectricCar()
electric_car.vehicle_method()      
electric_car.car_method()       
electric_car.electric_car_method() 

# OUTPUT:

# This is a vehicle.
# This is a car.
# This is an electric car.

"""
Polymorphism with Functions


Q) Create two classes: 'Circle' and 'Square'.
Both should have a method called 'area()' that calculates and returns their respective areas.
Write a function 'print_area(shape)' that accepts an object and calls its 'area()' method.
Pass objects of both classes to this function and print the result.

"""
# ANSWER:

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calculates and returns the area of the circle"""
        return 3.14159 * (self.radius ** 2)

class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        """Calculates and returns the area of the square"""
        return self.side ** 2

def print_area(shape):
    print(f"The area of the shape is: {shape.area()}")

circle = Circle(5)
square = Square(4)

print_area(circle)
print_area(square)

# OUTPUT:

# The area of the shape is: 78.53975
# The area of the shape is: 16

# Q) A machine that takes user input for product name and tells the price of the product if it's available in the list.

# ANSWER:

products = {
    "Apple": 100,
    "Banana": 50,
    "Orange": 75,
    "Mango": 200,
    "Grapes": 150
}
def get_product_price(product_name):
    if product_name in products:
        return f"The price of {product_name} is {products[product_name]} PKR"
    else:
        return f"Sorry, {product_name} is not available or not for sale."
while True:
    product_name = input("Enter product name (or 'quit' to stop): ")
    if product_name.lower() == 'quit':
        break
    print(get_product_price(product_name.capitalize()))

# OUTPUT:

# Enter product name (or 'quit' to stop): apple
# The price of Apple is 100 PKR
# Enter product name (or 'quit' to stop): mango
# The price of Mango is 200 PKR
# Enter product name (or 'quit' to stop): peach
# Sorry, Peach is not available or not for sale.
# Enter product name (or 'quit' to stop): quit

# Q) Remove duplicates from list manually (without set).

# ANSWER:

def remove_duplicates(lst):
    new_lst = []
    for i in lst:
        if i not in new_lst:
            new_lst.append(i)
    return new_lst

lst = [1, 2, 2, 3, 4, 4, 5, 6, 6]
print(remove_duplicates(lst))  # [1, 2, 3, 4, 5, 6]

# OUTPUT:

# [1, 2, 3, 4, 5, 6]

# Q) Flatten a nested list using loop. 

# ANSWER:

def flatten(nested_lst):
    flat_lst = []
    for sublist in nested_lst:
        for item in sublist:
            flat_lst.append(item)
    return flat_lst
nested_lst = [[1, 2], [3, 4], [5, 6]]
print(flatten(nested_lst)) 

# OUTPUT:

# [1, 2, 3, 4, 5, 6]

# Q) Count number of urgent messages in chat logs. 

# ANSWER:

chat_logs = [
    {'message': 'Hello', 'urgent': False},
    {'message': 'Help!', 'urgent': True},
    {'message': 'How are you?', 'urgent': False},
    {'message': 'Emergency!', 'urgent': True}
]

urgent_count = 0
for log in chat_logs:
    if log['urgent']:
        urgent_count += 1
print(urgent_count) 

# OUTPUT:
# 2

# 53. Loop to show only Pakistani contacts (+92). 

# ANSWER:

contacts = [
    {'name': 'John', 'phone': '+1234567890'},
    {'name': 'Ali', 'phone': '+923123456789'},
    {'name': 'Jane', 'phone': '+9876543210'},
    {'name': 'Ahmad', 'phone': '+923987654321'}
]

pakistani_contacts = []
for contact in contacts:
    if contact['phone'].startswith('+92'):
        pakistani_contacts.append(contact)
print(pakistani_contacts)

# OUTPUT:

#[{'name': 'Ali', 'phone': '+923123456789'}, {'name': 'Ahmad', 'phone': '+923987654321'}]

# 54. Simulate inventory reduction when order placed. 

# ANSWER:

inventory = {'item1': 10, 'item2': 5, 'item3': 8}
order = {'item1': 2, 'item2': 1}

for item, quantity in order.items():
    if item in inventory:
        inventory[item] -= quantity
print(inventory)

# OUTPUT:

#{'item1': 8, 'item2': 4, 'item3': 8}

# 55. Loop through doctor profiles and print specialists only. 

# ANSWER:

doctors = [ {'name': 'Dr. Smith', 'specialty': 'Cardiology'},
    {'name': 'Dr. Johnson', 'specialty': 'General Practice'},
    {'name': 'Dr. Lee', 'specialty': 'Neurology'}]
specialists = []
for doctor in doctors:
    if doctor['specialty'] != 'General Practice':
        specialists.append(doctor)
print(specialists)

# OUTPUT:

# [{'name': 'Dr. Smith', 'specialty': 'Cardiology'}, {'name': 'Dr. Lee', 'specialty': 'Neurology'}]

# 56. Loop through dictionary of courses per student. 

# ANSWER:

students_courses = { 'John': ['Math', 'Science', 'English'],
    'Alice': ['History', 'Biology', 'Chemistry'],
    'Bob': ['Physics', 'Computer Science', 'Math']}
for student, courses in students_courses.items():
    print(f'{student}: {", ".join(courses)}')

# OUTPUT:

# John: Math, Science, English
# Alice: History, Biology, Chemistry
# Bob: Physics, Computer Science, Math

# Interview Qs: 

# 57. How do you iterate over both keys and values in dictionary?

# ANSWER:

my_dict = {'a': 1, 'b': 2, 'c': 3}
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")

# OUTPUT:

# Key: a, Value: 1
# Key: b, Value: 2
# Key: c, Value: 3



# Q) Remove duplicate characters from string (no set).

# ANSWER:

def remove_duplicates(s):
    result = ""
    for char in s:
        if char not in result:
            result += char
    return result

# Example usage:
s = "Programming"
print("Original string:", s)
print("String without duplicates:", remove_duplicates(s))

# OUTPUT:

# Original string: Programming
# String without duplicates: Progamin

# Q) Find first non-repeated character in string. 

# ANSWER:

def first_non_repeated(s):
    for char in s:
        if s.count(char) == 1:
            return char
    return None

# Example usage:
s = "none"
print("First non-repeated character:", first_non_repeated(s))

# OUTPUT:
# First non-repeated character: o

# Q) Rotate string left (`abc` → `bca`)

# ANSWER:

s = "abc"
print(s[1:] + s[0])

# OUTPUT:
# bca

# Q) Compress string (`aaabb` → `a3b2`). 

# ANSWER:

s = "aaabb"
result = ""
count = 1
for i in range(1, len(s)):
    if s[i] == s[i-1]:
        count += 1
    else:
        result += s[i-1] + str(count)
        count = 1
result += s[-1] + str(count)
print(result)

# OUTPUT:

# a3b2

# Q) Reverse words in sentence without slicing. 

# ANSWER:

sentence = "Hello World"
words = sentence.split()
reversed_words = [word[::-1] for word in words]
print(' '.join(reversed_words))

# OUTPUT:

# olleH dlroW

# Q) Count uppercase vs lowercase letters. 

# CODE:

s = "Hello World"
uppercase_count = sum(1 for c in s if c.isupper())
lowercase_count = sum(1 for c in s if c.islower())
print(f"Uppercase: {uppercase_count}, Lowercase: {lowercase_count}")

# OUTPUT:

# Uppercase: 2, Lowercase: 8

# Q) Validate password (min 8 chars, at least 1 digit). 

# CODE:

password = "Password123"
if len(password) >= 8 and any(c.isdigit() for c in password):
    print("Valid")
else:
    print("Invalid")

# OUTPUT:

# Valid

