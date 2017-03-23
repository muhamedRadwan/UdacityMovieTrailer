import Movie
import fresh_tomatoes

avatar = Movie.Movie("Avatar",  # the name of movie
                     "Avatar (marketed as James Cameron's Avatar) is a 2009 American[7][8] "
                     "epic science fiction film directed",  # description
                     "https://upload.wikimedia.org/wikipedia"
                     "/en/b/b0/Avatar-Teaser-Poster.jpg",  # the image
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY"  # youtube trailer link
                     )

# Description of movies saved in moveTile variable
moveTile = "Ice Age Continental Drift is a 2012 American 3D" \
           " computer-animated comedy adventure film produced by" \
           " Blue Sky Studios." \
           " It was written by Jason Fuchs and Michael Berg," \
           " and directed by Steve Martino and Michael Thurmeier " \
           "the first film in the series not to be directed " \
           "by Carlos Saldanha.[4]"
# first movie
iceEdge = Movie.Movie("Ice Edge 4",  # the name of movie
                      moveTile,  # description
                      "https://upload.wikimedia.org/wikipedia/en/thumb/6/6c/Ice_Age_Continental_Drift.jpg"
                      "/220px-Ice_Age_Continental_Drift.jpg",
                      # the image
                      "https://www.youtube.com/watch?v=0pdqf4P9MB8"  # youtube trailer link
                      )

moveTile = "Saw is a 2004 American psychological horror film[3][4] " \
           "directed by James Wan. It is Wan's feature film directorial debut."
# second movie
saw = Movie.Movie("Saw",  # the name of movie
                  moveTile,  # description
                  "https://upload.wikimedia.org/wikipedia/en/5/56/Saw_official_poster.jpg",  # the image
                  "https://www.youtube.com/watch?v=hzixp8s4pyg"  # youtube trailer link
                  )

moveTile = "The Expendables is an American series of action films written " \
           "by and starring Sylvester Stallone and originally created by David Callaham." \
           " The film series itself was created to pay homage to the blockbuster action films " \
           "of the 1980s and 90s and also pays gratitude to the action stars of those decades, " \
           "as well as more recent stars in action. The series consists of three films: The Expendables (2010), " \
           "The Expendables 2 (2012) and The Expendables 3 (2014), with a final" \
           " fourth film scheduled to be released in 2018. " \
           "The series has received mixed critical reception," \
           " in regard to its plots and dialogue between the characters; however," \
           " many critics praised the use of humor and action scenes. The films have been box office successes."
# third movie
theExpendables = Movie.Movie("The Expendables",  # the name of movie
                             moveTile,  # description
                             " https://upload.wikimedia.org/wikipedia/en/e/ed/The_Expendables_2_poster.jpg",
                             # the image
                             "https://www.youtube.com/watch?v=YU1ueHDC754"  # youtube trailer link
                             )

moveTile = "The Godfather is a 1972 American crime film directed by" \
           " Francis Ford Coppola and produced by Albert S. Ruddy," \
           " based on Mario Puzo's best-selling novel of the same name." \
           " It stars Marlon Brando and Al Pacino as the leaders of a fictional New York crime family. The story," \
           " spanning 1945 to 1955," \
           " chronicles the family under the patriarch Vito Corleone," \
           " focusing on the transformation of Michael Corleone (Pacino) " \
           "from reluctant family outsider to ruthless mafia boss."

# fourth movie
theGodfather = Movie.Movie("The Godfather",  # the name of movie
                           moveTile,  # description
                           "https://upload.wikimedia.org/wikipedia/en/1/1c/Godfather_ver1.jpg",  # the image
                           "https://www.youtube.com/watch?v=sY1S34973zA"  # youtube trailer link
                           )
# fifth movie
lalaLand = Movie.Movie("la la Land",  # the name of movie
                       "La La Land is a 2016 American musical film written and directed by Damien Chazelle",
                       # description
                       "https://upload.wikimedia.org/wikipedia/en/a/ab/La_La_Land_%28film%29.png",  # the image
                       "https://www.youtube.com/watch?v=0pdqf4P9MB8"  # youtube trailer link
                       )
# sit array of movies
movies = [avatar, iceEdge, saw, theExpendables, theGodfather, lalaLand]

# call th viewer function that display the movies
fresh_tomatoes.open_movies_page(movies)
