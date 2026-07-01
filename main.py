import requests
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY")

def search_movie(search_name):
    response = requests.get(f"http://www.omdbapi.com/?apikey={api_key}&s={search_name}")
    returned_data = response.json()
    for movie in returned_data.get("Search", []):
        print(f"Title: {movie['Title']}, Year: {movie['Year']}, IMDB ID: {movie['imdbID']}")

search_name = input("Enter a movie or series name to search: ")

if __name__ == "__main__":
    search_movie(search_name)