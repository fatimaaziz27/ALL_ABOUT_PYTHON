#                                   Exception Handling

# Division Error (ZeroDivisionError)

try:
   a = int(input("Enter first number: "))
   b = int(input("Enter second number: "))
  
   result = a / b
   print("Result is:", result)
except ZeroDivisionError:
   print("Cannot divide by zero!")
