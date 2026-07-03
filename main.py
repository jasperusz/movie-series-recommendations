import requests
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY")

def search_movie(search_name):
    response = requests.get(f"http://www.omdbapi.com/?apikey={api_key}&s={search_name}")
    returned_data = response.json()
    for i, movie in enumerate(returned_data.get("Search", []), start=1):
        print(f"{i}. Title: {movie['Title']}, Year: {movie['Year']}, IMDB ID: {movie['imdbID']}")
    while True:
        try:
            choice = int(input("Select the movie or series by selecting the number (or 0 to exit): "))
            if choice == 0:
                print("Exiting...")
                break
            elif 1 <= choice <= len(returned_data.get("Search", [])):
                selected_movie = returned_data["Search"][choice - 1]
                print(f"You selected: {selected_movie['Title']} ({selected_movie['Year']})")
                break
        except ValueError:
            print("Invalid input. Please enter a number corresponding to the movie or series on the list.")

search_name = input("Enter a movie or series name to search: ")

if __name__ == "__main__":
    while True:
        search_movie(search_name)
        print("Do you want to search for another movie or series? (yes/no)")
        continue_search = input().strip().lower()
        if continue_search != 'yes':
            print("Exiting...")
            break