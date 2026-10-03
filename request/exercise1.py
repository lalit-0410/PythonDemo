import requests

url="https://jsonplaceholder.typicode.com/users"

try:
    response=requests.get(url)

    
    response.raise_for_status()

    if response.status_code==200:
        data=response.json()
        print(data[0]["name"])
        print(data[0]["email"])
except requests.exceptions.RequestException as e:
    print("API error:", e)
