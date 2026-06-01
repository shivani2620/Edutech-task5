# Task 5 - File Handling & Automation

print("File Handling Automation Program")


# 1. Writing to a Text File

name = input("Enter your name: ")
course = input("Enter your course: ")

with open("student.txt", "w") as file:

    file.write("Student Information\n")
    file.write(f"Name: {name}\n")
    file.write(f"Course: {course}\n")

print("\nData written successfully to student.txt")


# 2. Appending Data

phone = input("\nEnter phone number: ")

with open("student.txt", "a") as file:

    file.write(f"Phone: {phone}\n")

print("Phone number appended successfully")


# 3. Reading File Data

print("\nReading File Content:\n")

with open("student.txt", "r") as file:

    content = file.read()
    print(content)


# 4. Error Handling

try:

    with open("unknown.txt", "r") as file:
        print(file.read())

except FileNotFoundError:

    print("Error: File does not exist")
