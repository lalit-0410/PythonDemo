import requests

url="https://jsonplaceholder.typicode.com/users"
user={
    "name":"Lalit",
    "course":"MCA",
    "skills":["JAVA","Python"]
}

response=requests.post(url,json=user)

if response.status_code==201:
    response.json()
    print(response.status_code)
