class Student:

    def __init__(self, name, age, course, marks):
        self.name = name
        self.age = age
        self.course = course
        self.marks = marks

    def calculate_average(self):
        return sum(self.marks) / len(self.marks)

    def display(self):
        print(
            f"Name: {self.name}, "
            f"Age: {self.age}, "
            f"Course: {self.course}, "
            f"Average: {self.calculate_average():.2f}"
        )


#Normal Function
def add_student(students):

    try:
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        course = input("Enter course: ")

        marks = list(map(int, input("Enter marks: ").split()))

        student = Student(name, age, course, marks)

        students.append(student)

        print("Student added successfully!")

    except ValueError:
        print("Please enter valid numbers.")


#Normal Function
def display_all(students):

    print("\n--- All Students ---")

    for student in students:
        student.display()


#Normal Function
def show_top_students(students):

    print("\n--- Students Above 60 ---")

    top_students = list(filter(lambda student: student.calculate_average() > 60,students))

    for student in top_students:
        student.display()

#Normal Function
def show_unique_courses(students):

    print("\n--- Unique Courses ---")

    courses = {student.course for student in students}

    print(courses)


students = []

add_student(students)
add_student(students)
add_student(students)

display_all(students)

show_top_students(students)

show_unique_courses(students)