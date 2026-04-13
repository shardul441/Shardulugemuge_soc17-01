# Write mode
with open("sample.txt", "w") as file:
    file.write("Hello, this is the first line in the file.\n")
    file.write("File handling in Python is easy to learn.\n")
print("Data written successfully.\n")

# Read mode
with open("sample.txt", "r") as file:
    print("Reading file contents:")
    print(file.read())

# Append mode
with open("sample.txt", "a") as file:
    file.write("This line is added using append mode.\n")
print("\nData appended successfully.\n")

# Read updated file
with open("sample.txt", "r") as file:
    print("Updated file contents:")
    print(file.read())