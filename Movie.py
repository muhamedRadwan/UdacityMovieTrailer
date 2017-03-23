import webbrowser
'''
this class provide
1-show trailer function that open the youtube trailer video for moves
2-object for movie film
'''


class Movie:
    # initialize object of movie
    def __init__(self, movie_name, storyline, poster_image, youtube_trailer):
        self.title = movie_name
        self.movieTile = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = youtube_trailer

    # show_trailer show trailer of movie
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
