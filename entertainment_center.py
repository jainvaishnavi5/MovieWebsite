import fresh_tomatoes
import media


# variable containing names of the movies
name = ["Toy Story", "Dangal", "Raees", "Minions",
        "Ratatouille", "3 Idiots"]

# variable containing storyline of the movies
story = ["A story of a boy and his toys come to life.",
         "Biographical on former wrestler Mahavir"
         " Singh Phogat and his two wrestler daughters.",
         "This film unfolds the story of a cruel and "
         "clever bootlegger, whose business is challenged"
         " by a tough cop.", "Scarlet and husband Herb,"
         " hatches a plot to take over the world.",
         "A rat who can cook struggles and works at a"
         " famous restaurant.", "Struggle and engineering "
         "life of three friends."]

# variable containing poster url of the movies
poster = ["https://upload.wikimedia.org/wikipedia/en/1/13/"
          "Toy_Story.jpg", "https://images-na.ssl-images-amazon."
          "com/images/M/MV5BMTQ4MzQzMzM2Nl5BMl5BanBnXkFtZTgwMTQ1N"
          "zU3MDI@._V1_QL50_SY1000_CR0,0,713,1000_AL_.jpg",
          "https://images-na.ssl-images-amazon.com/images/M/MV5BMTc2"
          "NTYwMTE1NV5BMl5BanBnXkFtZTgwODQ5MzAwMTI@._V1_QL50_S"
          "Y1000_CR0,0,761,1000_AL_.jpg",
          "http://www.impawards.com/2015/posters/minions_xlg.jpg",
          "https://images-na.ssl-images-amazon.com/images/M"
          "/MV5BMTMzODU0NTkxMF5BMl5BanBnXkFtZTc"
          "wMjQ4MzMzMw@@._V"
          "1_QL50_SY1000_CR0,0,674,1000_AL_.jpg",
          "https://images-na.ssl-images-amazon.com/images/M/MV5B"
          "ZWRlNDdkNzItMzhlZC00YTdmLWIwNjktYjY5"
          "NjQ1ZmQ3N2FkXkEyXkFqcGdeQ"
          "XVyNjU0OTQ0OTY@._V1_QL50_SY1000_CR0,0,747,1000_AL_.jpg"]

# variable containing trailer url of the movies
trailer = ["https://www.youtube.com/watch?v=4KPTXpQehio",
           "https://www.youtube.com/watch?v=x_7YlGv9u1g",
           "https://www.youtube.com/watch?v=J7_1MU3gDk0",
           "https://www.youtube.com/watch?v=eisKxhjBnZ0",
           "https://www.youtube.com/watch?v=niD-jahFURU",
           "https://www.youtube.com/watch?v=xvszmNXdM4w"]

# variable which will contain objects of the movies
movie_ob = []
for i in range(0, 6):
    movie_ob.append(media.Movie(name[i], story[i], poster[i], trailer[i]))
fresh_tomatoes.open_movies_page(movie_ob)
