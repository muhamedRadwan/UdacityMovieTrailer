import webbrowser
class Movie:
   def   __init__(self,movieName,storyline,posterImage,youtubeTrailer):
        self.title=movieName
        self.movieTile=storyline
        self.poster_image_url=posterImage
        self.trailer_youtube_url=youtubeTrailer


   def showTrailer(self):
      webbrowser.open(self.trailer_youtube_url)
