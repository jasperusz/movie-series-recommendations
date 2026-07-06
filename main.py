import requests
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY")

def search_movie(search_name):
    response = requests.get(f"http://www.omdbapi.com/?apikey={api_key}&s={search_name}")
    returned_data = response.json()
    if returned_data is None or returned_data.get("Response") == "False":
        print("No results found. Please try again.")
        return None
    for i, movie in enumerate(returned_data.get("Search", []), start=1):
        print(f"{i}. Title: {movie['Title']}, Year: {movie['Year']}")
    while True:
        try:
            choice = int(input("Select the movie or series by selecting the number (or 0 to exit/99 to search again): "))
            if choice == 0:
                print("Exiting...")
                return None
            elif choice == 99:
                print("Searching again...")
                return search_movie(input("Enter a movie or series name to search: "))
            elif 1 <= choice <= len(returned_data.get("Search", [])):
                selected_movie = returned_data["Search"][choice - 1]
                print(f"You selected: {selected_movie['Title']} ({selected_movie['Year']})")
                selected_movie_id = selected_movie['imdbID']
                break
        except ValueError:
            print("Invalid input. Please enter a number corresponding to the movie or series on the list.")
    return selected_movie_id

def get_details(movie_id):
    response = requests.get(f"http://www.omdbapi.com/?apikey={api_key}&i={movie_id}")
    info_data = response.json()
    movie_title = info_data.get("Title", "N/A")
    movie_year = info_data.get("Year", "N/A")
    movie_genre = info_data.get("Genre", "N/A")
    movie_director = info_data.get("Director", "N/A")
    movie_plot = info_data.get("Plot", "N/A")
    movie_rating = info_data.get("imdbRating", "N/A")
    movie_rated = info_data.get("Rated", "N/A")
    movie_country = info_data.get("Country", "N/A")
    return {
        "Title": movie_title,
        "Year": movie_year,
        "Genre": movie_genre,
        "Director": movie_director,
        "Plot": movie_plot,
        "Rating": movie_rating,
        "Rated": movie_rated,
        "Country": movie_country
    }

search_name = input("Enter a movie or series name to search: ")

if __name__ == "__main__":
    while True:
        movie_id = search_movie(search_name)
        if movie_id:
            details = get_details(movie_id)
            print("\nMovie/Series Details:")
            for key, value in details.items():
                print(f"{key}: {value}")

        print("Do you want to search for another movie or series? (yes/no)")
        continue_search = input().strip().lower()
        if continue_search != 'yes':
            print("Exiting...")
            break