import json
import os
student={
    "name":"Lalit",
    "age":25
}

#python obj to json obj
json_data=json.dumps(student)
print(json_data)

#json to python obj
json_data = '{"name": "Lalit", "age": 22}'
student=json.loads(json_data)
print(student)
print(student["name"])


#file handling with json
with open("student.json","w")as file:
    json.dump(student,file)
    print("Data inserted in json file")

with open ("student.json","r")as file:
    stdd=json.load(file)
    print("Data load....")
    print(stdd)
