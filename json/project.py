import json
name=input("Enter your name ")
age=int(input("Enter age"))
course=input("Course ")
skill=input("Enter skills: ").split()

student = {
    "name": name,
    "age": age,
    "course": course,
    "skills": skill
}

with open ("project.json","w")as file:
    json.dump(student,file)
    print("Data dumps in project file ")
# with open ("project.json","r")as file:
#     data=json.load(file)
#     print(data)

#     print(data["name"],data["skills"])