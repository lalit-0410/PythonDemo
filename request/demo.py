import requests

response = requests.get("https://api.github.com/events")

print("Status Code:", response.status_code)

print("Content Type:", response.headers["content-type"])

print("Encoding:", response.encoding)

print("Response as Text:")
print(response.text)

print("Response as JSON:")
print(response.json())