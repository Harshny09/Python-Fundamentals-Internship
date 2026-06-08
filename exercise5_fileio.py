# File Handling

with open("sample.txt", "w") as file:
    file.write("Welcome to Python Internship")

with open("sample.txt", "r") as file:
    content = file.read()

print(content)