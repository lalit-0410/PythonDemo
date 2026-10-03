import json


class Student:
    def __init__(self, name, age, course, skills):
        self.name = name
        self.age = age
        self.course = course
        self.skills = skills

    def show(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Course: {self.course}")
        print(f"Skills: {self.skills}")


def add_student():
    try:
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        course = input("Enter course: ")
        skills = input("Enter skills using space: ").split()

        student = Student(name, age, course, skills)
        students.append(student)

        print("Student added successfully!")

    except ValueError as e:
        print("Error:", e)


def student_to_dict(student):
    return {
        "name": student.name,
        "age": student.age,
        "course": student.course,
        "skills": student.skills
    }


def save_students(students):
    data = []

    for student in students:
        data.append(student_to_dict(student))

    with open("student.json", "w") as file:
        json.dump(data, file, indent=4)

    print("Students saved!")


def display_students(students):
    if not students:
        print("No students found.")
        return

    for student in students:
        student.show()


def load_students():
    try:
        with open("student.json", "r") as file:
            data = json.load(file)

        students = []

        for item in data:
            student = Student(
                item["name"],
                item["age"],
                item["course"],
                item["skills"]
            )

            students.append(student)

        return students

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        print("JSON file is empty or invalid.")
        return []


# Load existing students when program starts
students = load_students()


while True:

    print("\n===== Student Manager =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Save Students")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students(students)

    elif choice == "3":
        save_students(students)

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")