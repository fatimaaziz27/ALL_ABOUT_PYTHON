#         Exception Handling

# Division Error (ZeroDivisionError)

try:
   a = int(input("Enter first number: "))
   b = int(input("Enter second number: "))
  
   result = a / b
   print("Result is:", result)
except ZeroDivisionError:
   print("Cannot divide by zero!")

# OUTPUT:
# Enter first number: 7
# Enter second number: 7
# Result is: 1.0

# Multiple Exceptions

try:
   num = int(input("Enter a number: "))
   result = 10 / num
   print("Result:", result)
except ValueError:
   print("Invalid number!")
except ZeroDivisionError:
   print("Cannot divide by zero!")
   
# OUTPUT:
# Enter a number: 7
# Result: 1.4285714285714286

# Using else

try:
   num = int(input("Enter a number: "))
except:
   print("Error occurred!")
else:
   print("You entered:", num)

# OUTPUT:
# Enter a number: 8
# You entered: 8

# Using finally

try:
   num = int(input("Enter a number: "))
   print("Number:", num)
except:
   print("Invalid input!")
finally:
   print("This block always runs")

# OUTPUT:
# Enter a number: 8
# Number: 8
# This block always runs

# Custom Message with Exception

try:
   num = int(input("Enter a number: "))
   print(100 / num)
except Exception as e:
   print("Error:", e)
   
# OUTPUT:
# Enter a number: 5
# 20.0
