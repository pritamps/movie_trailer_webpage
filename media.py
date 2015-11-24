import urllib, json

class OmdbTitle:
    """
    Class to wrap data from the OMDB API, which is an Open IMDB wrapper that
    gives access to IMDb data
    """
    OMDB_BASE_URL = "http://www.omdbapi.com/?i="
    OMDB_URL_SUFFIX = "&plot=short&r=json"

    def __init__(self, imdb_title_number = None):
        """

        :param imdb_title_number: Title number of the movie in IMDb
        :return:
        """
        self.imdb_title_number = imdb_title_number

        # Get movie data from OMDB database
        url = self.OMDB_BASE_URL + self.imdb_title_number + self.OMDB_URL_SUFFIX
        response = urllib.urlopen(url)
        self.json_data = json.loads(response.read())

    def get_movie_title(self):
        """
        :return: Movie title
        """
        return self.json_data['Title']

    def get_poster_image_url(self):
        """
        :return: Poster URL as string
        """
        return self.json_data['Poster']

    def get_actors(self):
        """
        :return: Actors in movie as single string
        """
        return self.json_data['Actors']

class Movie:
    """
    This class provides a data structure to represent a movie in an
    entertainment center, i.e. all movie data that can be obtained and
    displayed on a website.

    The idea is to have as few inputs to this constructor as possible.
    Currently, the constructor takes as input:
        1/ The IMDb title ID (which is a unique identifier for the movie)
        2/ The youtube URL for the trailer.
    TODO: Currently, there is no implementation of directly obtaining the
    youtube trailer URL directly from the IMDb title ID, or the IMDb the
    title ID from a Movie title (since the Title may not be unique). This
    needs to be investigated.
    """


    def __init__(self, imdb_title_number = None, trailer_youtube_url = None):
        """

        :param imdb_title_number: String representing IMDb title, eg "tt4110568"
        :param trailer_youtube_url: Youtube URL for trailer
        :return:
        """
        if not imdb_title_number:
            raise Exception, "IMDB Title Number needs to be specified"

        if not trailer_youtube_url:
            raise Exception, "Youtube URL needs to be specified for trailer"


        self.trailer_youtube_url = trailer_youtube_url

        # Get movie data from OMDB database
        omdb_title = OmdbTitle(imdb_title_number)

        # Populate movie data from OMDB
        self.title = omdb_title.get_movie_title()
        self.poster_image_url = omdb_title.get_poster_image_url()
        self.actors = omdb_title.get_actors()




