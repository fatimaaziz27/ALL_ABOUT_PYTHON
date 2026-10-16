# ASSIGNMENT 1 (PYTHON)
# Variables & Data Types (Q1–Q10) 

# 1. Create a variable `student_name`, assign your name, and print its type. 
# code:
student_name="fatima aziz"
print(type(student_name))
# Output:
# <class 'str'>

# 2. Store your age in a variable. Multiply it by 2 and print the result. 
# code:
age=18
print(age*2)
# Output:
# 36

# 3. Create three variables with an integer, a string, and a float. Print their types.
# code:

x="yusra"
y=16
z=3.14
print(type(x))
print(type(z))
print(type(y))
# Output:
# <class 'str'>
# <class 'float'>
# <class 'int'>

# 4. Convert the integer `5j5` to a string and concatenate with " is a number".
# code:
x = str("12")
print(x +" "+"is a number")
# Output:
# 12 is a number

# 5. Input two numbers, print their sum and the type of the result.
# code:
x = int(input('enter a number'))
y = int(input('enter a number'))
print(x+y)
print(type(x) , type(y))
# Output:
# enter a number
# 8
# enter a number
# 9
# 17
# <class 'int'> <class 'int'>

# 6. Assign `a = "5"` (string) and `b = 3`. Add them correctly and explain the result.
# Explanation:
# If we used 
a = "5"
b = 3
print(a+b)
# would result in a TypeError, because Python can't add strings and integers together. 
# To fix this, we use the int() function to convert the string "5" to an integer, like this: a = int("5"). 
# Then, print(a+b) works correctly and outputs 8.
a = int ("5")
b = 3
print(a+b)
# Output:
# 8

# 7. Swap values of two variables without a third variable. 
# code:
a = 5
b = 6
print(a)
print(b)
a,b = b,a
print(f"value after swapping variable a = {a}")
print(f"value after swapping variable b = {b}")
# Output:
# 5
# 6
# value after swapping variable a = 6
# value after swapping variable b = 5

# 8. What is the type and output of: `result = 3 + 4.0 + True`? 
# code:
result = 56 + 4.53 + True
print(f"the output is {result}")
print(f"the type of output is {type(result)}")
# Output:
# the output is 61.53
# the type of output is <class 'float'>

# 9. Input a float number and print if it’s an integer (without using `int()`). 
# code:
num=float(input("enter a decimal number:"))
if num%1==0:
    print("The number is an integer")
else:
    print("The number is not an integer.")
# Output:
# enter a decimal number:
# 6.7
# The number is not an integer.

# 10. Use `isinstance()` to check whether an input is float or integer. 
# code:
x = isinstance(4.6456, (float, int,))
print(x)
if x==False:
    print("The object is neither an integer nor a float.")
else:
    print("The object is either an integer or a float.")
# Output:
# True
# The object is either an integer or a float.

# Conditions (if/elif/else) (Q11–Q20) 

# 11. Check if a number is positive, negative, or zero. 
# Code:
num = int(input("enter a number:"))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
# Output:
# enter a number:
# 0
# Zero

# 12. Input marks; print "Passed" if ≥50, else "Failed". 
# Code:
marks = int(input("Enter marks:"))
if marks >= 50:
    print("Passed")
else:
    print("Failed")
# Output:
# Enter marks:
# 75
# Passed

# 13. Find the largest of three numbers using if/elif/else.
# Code:
num1 =int(input("Enter first number:"))
num2 =int(input("Enter second number:"))
num3 =int(input("Enter third number:"))
if num1 >= num2 and num1 >= num3:
    print(f"The largest number is {num1}.")
elif num2 >= num1 and num2 >= num3:
    print(f"The largest number is {num2}.")
else:
    print(f"The largest number is {num3}.")
# Output:
# Enter first number:
# 30
# Enter second number:
# 59
# Enter third number:
# 49
# The largest number is 59.

# 14. Input age. Print: Child (age <13), Teen (13–19), Adult (20+).
# Code:
age=int(input("Enter age: "))
if age < 13:
    print("Child")
elif  age <= 19:
    print("Teen")
else:
    print("Adult")
# Output:
# Enter age: 
# 18
# Teen

# 15. Check whether a number is even or odd using `%`. 
# Code:
n=int(input("enter a number:"))
if n % 2 == 0:
    print(f"{n} is an even number")
else:
    print(f"{n} is an odd number")
# Output:
# enter a number:
# 6
# 6 is an even number

# 16. Input two subjects' marks. Print: “Both Passed”, “One Passed”, or “None Passed”.
# Code:
math=int(input("Enter marks for math:"))
computer=int(input("Enter marks for computer:"))
if math >= 50 and computer >= 50:
    print("Both Passed")
elif math >= 50 or computer >= 50:
    print("One Passed")
else:
    print("None Passed")
# Output:
# Enter marks for math:
# 50
# Enter marks for computer:
# 60
# Both Passed

# 17. Classify a triangle as Equilateral, Isosceles, or Scalene using its sides.
# Code:
a =int(input("Enter side a:"))
b =int(input("Enter side b:"))
c =int(input("Enter side c:"))
if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("The triangle is Equilateral")
    elif a == b or b == c or a == c:
        print("The triangle is Isosceles")
    else:
        print("The triangle is Scalene")
else:
    print("The sides do not form a valid triangle.")
# Output:
# Enter side a:
# 6
# Enter side b:
# 6
# Enter side c:
# 6
# The triangle is Equilateral

# 18. Input a number. Print "Fizz" if divisible by 3, "Buzz" if 5, "FizzBuzz" if both.
# Code:
num =int(input("Enter a number: "))
if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print("not divisible by either 3 or 5")
# Output:
# Enter a number: 
# 2
# not divisible by either 3 or 5

# 19. Input temperature. Print: Freezing (<0), Cold (0–15), Moderate (16–30), Hot (>30).
# Code:
temp = float(input("Enter temperature: "))
if temp < 0:
    print("Freezing")
elif temp <= 15:
    print("Cold")
elif temp <= 30:
    print("Moderate")
else:
    print("Hot")
# Output:
# Enter temperature: 
# 12
# Cold

# 20. Validate username and password: Username ≥5 chars, Password has 1 digit and 1 special char.
# Code:
user_name=str(input("enter user name:"))
password=str((input("enter password:")))
if len(user_name) >= 5:
    print("Username is valid")
else:
    print("Username should be at least 5 characters long.")
if any(char.isdigit() for char in password) and any(char in "!@#$%^&*(),.?\":{}|<>" for char in password):
    print("Password is valid")
else:
    print("Password should have at least one digit and one special character.")
# Output:
# enter user name:
# hhhhh
# enter password:
# 123()*hf
# Username is valid
# Password is valid
 
# Lists (Q21–Q27) 

# 21. Create a list of 5 favorite fruits. Print the 3rd fruit. 
# Code:
favorite_fruits = ["mango","grapes","pineapple","dragon fruit","custard apple"]
print(favorite_fruits[2])
# Output:
# pineapple

# 22. Add a new fruit to the end. Print updated list. 
# Code:
favorite_fruits = ["mango","grapes","pineapple","dragon fruit"]
print(f"original list: {favorite_fruits}")
favorite_fruits.append("custard apple")
print(f"updated list: {favorite_fruits}")
# Output:
# original list: ['mango', 'grapes', 'pineapple', 'dragon fruit']
# updated list: ['mango', 'grapes', 'pineapple', 'dragon fruit', 'custard apple']

# 23. Remove the 2nd item. Print the list. 
# Code:
favorite_fruits = ["mango","grapes","pineapple","dragon fruit"]
print(f"original List: {favorite_fruits}")
favorite_fruits.pop(1)
print(f"Updated List: {favorite_fruits}")
# Output:
# original List: ['mango', 'grapes', 'pineapple', 'dragon fruit']
# Updated List: ['mango', 'pineapple', 'dragon fruit']

#  24. Sort the list alphabetically and print it. 
# Code:
favorite_fruits = ["mango","grapes","pineapple","dragon fruit"]
print(f"Original List: {favorite_fruits}")
favorite_fruits.sort()
print(f"Sorted List: {favorite_fruits}")
# Output:
# Original List: ['mango', 'grapes', 'pineapple', 'dragon fruit']
# Sorted List: ['dragon fruit', 'grapes', 'mango', 'pineapple']

# 25. Replace all even numbers in a list of 5 numbers with "Even" using a loop. 
# Code:
numbers = [1,2,3,4,5,6,7,8]
print(f"Original List: {numbers}")
for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        numbers[i] = "Even"
print(f"Updated List: {numbers}")
# Output:
# Original List: [1, 2, 3, 4, 5, 6, 7, 8]
# Updated List: [1, 'Even', 3, 'Even', 5, 'Even', 7, 'Even']

# 26. Write a function that returns a new list with only unique elements.
# Code:
import random
x = [8, 5, 3, 9, 2, 45, 14, 83, 65]
unique_list = list(set(x))
print(f"Original List: {x}")
print(f"Unique Elements: {unique_list}")
# Output:
# Original List: [8, 5, 3, 9, 2, 45, 14, 83, 65]
# Unique Elements: [65, 2, 3, 5, 8, 9, 45, 14, 83]

# 27. Sort a list of words by word length (not alphabetically). 

# Tuples (Q28–Q32) 

# 28. Create a tuple of 5 countries. Try changing the 2nd country and observe what happens. 
# Code:
thistuple = ("Switzerland", "Japan", "United States", "Canada", "Australia")
y = list(thistuple)
y[1] = "France"
thistuple = tuple(y)
print(thistuple)
# Output:
# ('Switzerland', 'France', 'United States', 'Canada', 'Australia')

# 29. Print the last two countries using slicing.
# Code:
thistuple = ("Switzerland", "Japan", "United States", "Canada", "Australia")
print(thistuple[3:5])
# Output:
# ('Canada', 'Australia')

# 30. Count how many times "Pakistan" appears in a tuple. 
# Code:
countries = ["pakistan","Canada","pakistan","Australia","pakistan","United States","pakistan","Switzerland","pakistan","Japan","pakistan"]
x = countries.count("pakistan")
print(x)
# Output:
# 6

# 31. Given: `t = (1, 2, 3, [4, 5])`. Add 6 to the list inside the tuple and explain the result. 
# Code:
t = (1, 2, 3, [4, 5])
t[3].append(6)
print(t)
# Output:
# (1, 2, 3, [4, 5, 6])
# Explanation:
# The tuple t itself is not being changed, but the list inside the tuple is being modified. 
# This works because tuples in Python are immutable, but they can contain mutable objects like lists. 
# When we modify the list inside the tuple, we are not changing the tuple itself,
# but rather the list object that the tuple references.

# 32. Convert tuple `(1, 2, 3)` to string "1-2-3" using `join()`.
# Code:
Tuple = ("John", "Peter", "Vicky")
x = "-".join(Tuple)
print(x)
# Output:  John-Peter-Vicky

# Dictionaries (Q33–Q38) 

# 33. Create dictionary `student` with keys: `name`, `age`, `grade`. Print all key-value pairs.
# Code:
student= {'name:fatima','age:65','grade:fifth'}
print(student)
# Output:
# {'grade:fifth', 'name:fatima', 'age:65'}

# 34. Add new key `subject` to the dictionary. Print updated dictionary.
# Code:
student= {'name : fatima','age : 65','grade : fifth'}
student.update({"subject : CS"})
print(student)
# Output:
# {'subject : CS', 'grade : fifth', 'age : 65', 'name : fatima'}

# 35. Search for a key. If found, print the value. 
# Code:
student={'grade : fifth', 'age : 65', 'name : fatima'}
if "subject" in student:
    print("Yes, 'subject' is one of the keys in the student dictionary")
else:
    print("The 'subject' key is not in the student dictionary.")
# Output:
# The 'subject' key is not in the student dictionary.

# 36. Create dictionary of 3 students and their marks. Calculate average.
# Code:
students = {'yusra': 80,'asfiya': 90,'zainab': 70}
average = (80 + 90 + 70) / 3
print("Average:", average)
# Output:
# Average: 80.0

# 37. Given items and prices in a dictionary, input a budget and list affordable items. Given: 
marks = {"Ali": 45, "Sara": 70, "Shayan": 65, "Osama": 30} 
# Print students scoring ≥50. 
# Count how many failed. 

# Interview & Conceptual (Q39–Q50) 

# 38. What’s the difference between mutable and immutable types? Give examples.
# Answer:
# Mutable  Types: Can be changed after created and can be modified 
# Examples: lists, dictionaries, sets
# Immutable  Types: Cannot be changed after created and cannot be modified in-place; instead, a new object is created
# Examples: integers, floats, strings, tuples

# 39. Explain the difference between `is` and `==` in Python. 
# Answer:
print(a == b): # This statement checks if the values of a and b are equal. If a = [1, 2, 3] and b = [1, 2, 3], then a == b would be True because the values are the same.
print(a is b): # This statement checks if a and b are the same object in memory. If a = [1, 2, 3] and b = [1, 2, 3], then a is b would be False because a and b are two separate objects in memory, even though they have the same values.
# The statement print(a is a) would always be True, regardless of the value of a. This is because a is a is checking if a is the same object as itself, which is always the case.
# For example:
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)          # Output: True
print(a is b)           # Output: False
print(a is a)           # Output: True

# 40. Can you change values in a tuple? Why or why not? 
# Answer:
# No, you cannot change values in a tuple.
# Tuples are immutable in Python, which means their contents cannot be modified after creation.
# When you try to modify a tuple, you'll get a TypeError.

# 41. Explain how `elif` works. Can it exist without `if`? 
# Answer:
# It's used to check another condition if the initial if condition is false If the if condition is false, 
# the program will then check the elif condition If the elif condition is true, the code under it will be executed.
# No, elif cannot exist without if. elif is a part of the if-elif-else statement and is used to extend the if statement.

# 42. What happens when accessing a non-existent dictionary key? How to avoid it?
# Answer:
# When you try to access a key that doesn't exist in a dictionary, Python will raise a KeyError.
# To avoid it, check if the key exists or use other methods like get().

# 43. Why are strings immutable in Python? What are the benefits? 
# Answer:
# Strings are immutable in Python for security, thread safety, performance, and code integrity. It makes code more predictable, efficient, and secure.
# The benefits of immutable strings in Python are:
# Code predictability: Immutable strings ensure that string data remains consistent and predictable.
# Memory efficiency: Immutable strings can be reused and cached, reducing memory usage.
# Security: Immutable strings reduce the risk of sensitive data being modified after creation.

# 44. Difference between `list.copy()` and using `=` assignment? Show example.
# Answer:
# list.copy() creates a new, independent copy of the original list.
# “=” is used to assign a reference to the original list, not create a new copy.
# Example:
original_list = [1, 2, 3]
new_list1 = original_list            #Here original_list1 is assigned to new_list variable
new_list2 = original_list.copy()             #new copy

# 45. Can a tuple contain mutable items? Give a code example. 
# Answer:
# yes tuple can contain mutable items
# code example:
# Code Example:
t = (1, 2, 3, [4, 5, 6, 7])

# 46. What is the difference between `in` when used in a list vs a dictionary?
# Answer:
# The in operator behaves differently when used with lists and dictionaries.
# Lists: in checks if a value is present in the list.
# Dictionaries: in checks if a key is present in the dictionary.

# 47 Explain shallow copy vs deep copy with a list example. 
# Answer:
# When copying a list, you can use either shallow copy or deep copy.
# Shallow Copy: Creates a new list and copies the references of the original elements. If the original list contains mutable elements (like lists or dictionaries), modifying those elements in the copied list will affect the original list.
# Deep Copy: Creates a new list and recursively copies the elements. Modifying any element in the copied list will not affect the original list.
# Code Example:
import copy
original_list = [[1, 2], [3, 4]]

#Shallow Copy example

shallow_copied_list = copy.copy(original_list)
shallow_copied_list[0][0] = 'X'
print(original_list)  
print(shallow_copied_list) 

#Deep Copy example

original_list = [[1, 2], [3, 4]]
deep_copied_list = copy.deepcopy(original_list)
deep_copied_list[0][0] = 'X'
print(original_list) 
print(deep_copied_list) 

# 48. What is the output of: 
x = [1, 2, 3] 
y = x 
y.append(4) 
print(x) 
# Explain the result.
# Answer:
# x = [1, 2, 3]: Creates a list [1, 2, 3] and assigns it to x.
# y = x: Assigns the reference of x to y, so both x and y point to the same list object.
# y.append(4): Updates the list by adding 4 to it.
# print(x): Prints the updated list [1, 2, 3, 4].
# Output:
# [1, 2, 3, 4]

# The output is [1, 2, 3, 4] because y = x assigns the same memory reference to y as x, so both variables point to the same list. When you append 4 to y, you're modifying the same list that x references, resulting in x also reflecting the change.
