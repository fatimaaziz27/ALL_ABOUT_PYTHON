#                                   Exception Handling

# Division Error (ZeroDivisionError)

try:
   a = int(input("Enter first number: "))
   b = int(input("Enter second number: "))
  
   result = a / b
   print("Result is:", result)
except ZeroDivisionError:
   print("Cannot divide by zero!")
   
# Multiple Exceptions

try:
   num = int(input("Enter a number: "))
   result = 10 / num
   print("Result:", result)
except ValueError:
   print("Invalid number!")
except ZeroDivisionError:
   print("Cannot divide by zero!")

# Using else
try:
   num = int(input("Enter a number: "))
except:
   print("Error occurred!")
else:
   print("You entered:", num)

