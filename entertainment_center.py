# Simple script to generate a webpage based on json input.
# The

import json
import media
import fresh_tomatoes
import optparse

def open_movies_page(path_to_file):
    # Load data from JSON file
    with open(path_to_file) as data_file:
        json_data = json.load(data_file)
        imdb_titles = json_data["movies"]

    # Generate list of movies
    movies = []
    for title in imdb_titles:
        movie = media.Movie(title["imdb_title_number"],
                            title["trailer_url"])
        movies.append(movie)

    # Creates and opens the movies webpage
    fresh_tomatoes.open_movies_page(movies)

if __name__ == "__main__":
    parser = optparse.OptionParser()

    parser.add_option("-f", "--file", dest="path_to_file",
                      default="movielist_data.json")

    (options, args) = parser.parse_args()
    open_movies_page(options.path_to_file)


