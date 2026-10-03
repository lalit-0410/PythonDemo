import os
from dotenv import find_dotenv, load_dotenv

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

print(os.getenv("API_KEY"))
print(os.getenv("PASSWORD"))