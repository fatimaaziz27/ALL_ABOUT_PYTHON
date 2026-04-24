#             FILE HANDLING

# Append to File

file = open("test.txt", "a")
file.write("\nThis is new added text")
file.close()

file = open("test.txt", "r")
print(file.read())
file.close()
