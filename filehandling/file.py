import os

# 1. CREATE + WRITE FILE
print("----- CREATE AND WRITE -----")

with open("student.txt", "w") as file:
    file.write("Lalit\n")
    file.write("Rahul\n")
    file.write("Aman\n")

print("File created and data written successfully.")


# 2. READ FILE
print("\n----- READ FILE -----")

with open("student.txt", "r") as file:
    data = file.read()
    print(data)


# 3. tell()
print("----- TELL -----")

with open("student.txt", "r") as file:
    print("Initial position:", file.tell())

    file.read(5)

    print("Position after reading 5 characters:", file.tell())


# 4. seek()
print("\n----- SEEK -----")

with open("student.txt", "r") as file:
    print("First 5 characters:", file.read(5))

    file.seek(0)

    print("After seek(0):", file.read(5))


# 5. RENAME FILE
print("\n----- RENAME -----")

old_name = "student.txt"
new_name = "students.txt"

if os.path.exists(old_name):
    os.rename(old_name, new_name)
    print("File renamed successfully.")


# # 6. DELETE FILE
# print("\n----- DELETE -----")

# if os.path.exists(new_name):
#     os.remove(new_name)
#     print("File deleted successfully.")
# else:
#     print("File does not exist.")