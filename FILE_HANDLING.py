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

