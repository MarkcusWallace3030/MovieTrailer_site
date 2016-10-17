# Module to open the web browser from our code.

import webbrowser 

""" Here is the code to create the class that stores our blue
print data for the movie class
"""


class Movie1():
    def __init__(self, movie_title, movie_storyline, movie_posterImage,
                 movie_trailer,):
         # Instance variable that displays the title of the movie
        self.title = movie_title
        # Instance variable that displays the storyline of the selected video
        self.storyline = movie_storyline
        self.poster_image_url = movie_posterImage
        # Instance variable that displays the jpeg of the movie class Instance.
        self.trailer_youtube_url = movie_trailer
    # Instance varible that is pointed to a url link of an instance
    # in the mmovie class.
    
    # This Instance Method plays the movie trailer when the user clicks
    # on a poster image on the web page.
    
    def show_trailer(self):
        webbrowser.open(self.trailer_youtbue_url)

# imports a method from the webbrowser class
# to open a url pointed to one of our movies in the Movie class.


