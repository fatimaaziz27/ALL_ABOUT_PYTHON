# Q1) What will be the output of the following code?

age=20
if age >= 18:
    if age >= 65:
        print("senior citizen")
    else:
        print("Adult")
else:
    print("Minor")

# OUTPUT:
# Adult

# Q2) What will be the output of the following code?

is_raining = False
if not is_raining:
    print("go outside")
else:
    print("stay inside")

# OUTPUT:
# go outside

# Q3) What will be the output of the following code?

word = "python"
if word == "python":
    print("lowercase match")
elif word.lower() == "python":
    print("case insensitive match") 
else:
    print("no match")

# OUTPUT:
# lowercase match

# Q4) What will be the output of the following code?

fruit = ["apple", "banana", "cherry"]
if "banana" in fruit:
    print("banana is available")
else:
    print("banana is missing")

# OUTPUT:
# banana is available

# Q5) What will be the output of the following code?

person = {"name": "Alice", "age": 30}
if "age" in person:
    print("age is present")
else:
    print("age is missing")

# OUTPUT:
# age is present

# Q6) What will be the output of the following code?

balance = 500
withdraw = 200
if withdraw > 0:
