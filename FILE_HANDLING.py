#             FILE HANDLING

# Append to File

file = open("test.txt", "a")
# Opens the file test.txt in append mode (a).
# Append mode adds new data at the end of the file without deleting old data.
file.write("\nThis is new added text")
# Writes a new line of text into the file.
# \n moves the text to the next line.
file.close()
# Closes the file after writing.
file = open("test.txt", "r")
# Opens the file in read mode (r).
print(file.read())
# Reads and prints all contents of the file.
file.close()
# Closes the file after reading.


# Write Multiple Lines

file = open("data.txt", "w")
# Opens the file data.txt in write mode (w).
# If the file already exists, old content is erased.
# If the file does not exist, a new file is created.
file.write("Line 1\nLine 2\nLine 3")
# Writes 3 lines into the file.
# \n is used to move to the next line.
file.close()
# Closes the file after writing.
file = open("data.txt", "r")
# Opens the file in read mode (r).
print(file.read())
# Reads and prints all file contents.
# Output:
# Line 1
# Line 2
# Line 3
file.close()
# Closes the file after reading.


# Read Line by Line

file = open("data.txt", "r")

for line in file:
   print(line)

file.close()

# Using with (Best Practice)

with open("test.txt", "w") as file:
   file.write("Using with statement")

with open("test.txt", "r") as file:
   print(file.read())

