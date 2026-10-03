import os

name=input("Enter name ")
course=input("Course ")
sentence=input("Enter a message ")

with open("demo.txt","w")as file:
    file.write(f"Name{name}")
    file.write(f"Course {course}")
    file.write(f"Message {sentence}")

with open("demo.txt", "r") as file:
    print("File content")
    print(file.read())
