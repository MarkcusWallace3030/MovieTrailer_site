# import statements to enable the classes we need to call

import fresh_tomatoes   # Python code with embedded html to display our movies
# in the webbrowser.
import media_data   # Python code that contains our Movie master class

# The following code includes instances of the Movie class. These instances are
# the movie title, storyline, image and trailer urls that were all defined
# in the media_data python file.


grandmas_boy = media_data.Movie1("GrandMa's Boy",  # trailing whitespace?
                                 "Classic Comedy.",  # noqa
                                 "http://www.gstatic.com/tv/thumb/movieposters/159810/p159810_p_v7_ad.jpg", # noqa
                                 "https://www.youtube.com/watch?v=Bi5CfCHknZs")

matrix = media_data.Movie1("Matrix", "Class Scifi Thriller.",
                           "http://t0.gstatic.com/images?q=tbn:ANd9GcQq3pIz-aKgkmYX1dJ-EL-AlHSPcOO7wdqRIJ5gJy9qNinXpmle", # noqa
                           "https://www.youtube.com/watch?v=vKQi3bBA1y8")

coming_to_america = media_data.Movie1("Coming To America", "Classic Comedy.",
                                      "http://t2.gstatic.com/images?q=tbn:ANd9GcRVQibXx0OsF_6xoE3FUPoMrmcjw19NZJqivD9Xaeq4juHaZ_n2", # noqa
                                      "https://www.youtube.com/watch?v=fqfJqLFQSIk") # noqa

school_of_rock = media_data.Movie1("School of Rock", "Classic Jack Black.",
                                   "http://www.gstatic.com/tv/thumb/movieposters/33094/p33094_p_v7_aa.jpg", # noqa
                                   "https://www.youtube.com/watch?v=3PsUJFEBC74") # noqa

paid_in_full = media_data.Movie1("Paid in Full", "Thiller",
                                 "http://www.gstatic.com/tv/thumb/dvdboxart/30004/p30004_d_v7_aa.jpg", # noqa
                                 "https://www.youtube.com/watch?v=Y63NfERYsL4&oref=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DY63NfERYsL4&has_verified=1") # noqa
inception = media_data.Movie1("Inception",
                              "Classic Thriller",
                              "http://t2.gstatic.com/images?q=tbn:ANd9GcRo9vfJCM6dzPkZHIHBVCtlJnAnew9Ai26kEdrli0-tfmatmciD", # noqa
                              "https://www.youtube.com/watch?v=JE9z-gy4De4")

# The following line of code is an array of the Movie1 instances.
# Each of these instances display on the webpage as their image screenshot url.

movies = [coming_to_america, school_of_rock, paid_in_full, inception,
          grandmas_boy, matrix]

# The following code calls a method from the fresh tomatoes python file and use
# s a open_movies_page method that displays our movies array on the html page.

fresh_tomatoes.open_movies_page(movies)





