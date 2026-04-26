#             FILE HANDLING

# Append to File

file = open("test.txt", "a")
file.write("\nThis is new added text")
file.close()

file = open("test.txt", "r")
print(file.read())
file.close()

# Write Multiple Lines

file = open("data.txt", "w")
file.write("Line 1\nLine 2\nLine 3")
file.close()

file = open("data.txt", "r")
print(file.read())
file.close()
