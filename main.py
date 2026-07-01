import requests
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY")

response = requests.get(f"http://www.omdbapi.com/?apikey={api_key}&s=Batman")

print(response.json())