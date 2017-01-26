import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=4KPTXpQehio")

#print(toy_story.storyline)
#toy_story.show_trailer()

dangal = media.Movie("Dangal",
                    "Biographical sports drama on former wrestler Mahavir Singh Phogat and his two wrestler daughters' struggle towards glory at the Commonwealth Games in the face of societal oppression.",
                    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTQ4MzQzMzM2Nl5BMl5BanBnXkFtZTgwMTQ1NzU3MDI@._V1_QL50_SY1000_CR0,0,713,1000_AL_.jpg",
                    "https://www.youtube.com/watch?v=x_7YlGv9u1g")

raees = media.Movie("Raees",
                    "Criticizing the prohibition of alcohol, prostitution and illegal drugs in Gujarat, this film unfolds the story of a cruel and clever bootlegger, whose business is challenged by a tough cop.",
                    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTc2NTYwMTE1NV5BMl5BanBnXkFtZTgwODQ5MzAwMTI@._V1_QL50_SY1000_CR0,0,761,1000_AL_.jpg",
                    "https://www.youtube.com/watch?v=J7_1MU3gDk0")

minions = media.Movie("Minions",
                    "Minions Stuart, Kevin and Bob are recruited by Scarlet Overkill, a super-villain who, alongside her inventor husband Herb, hatches a plot to take over the world.",
                    "http://www.impawards.com/2015/posters/minions_xlg.jpg",
                    "https://www.youtube.com/watch?v=eisKxhjBnZ0")

ratatouille = media.Movie("Ratatouille",
                    "A rat who can cook makes an unusual alliance with a young kitchen worker at a famous restaurant.",
                    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTMzODU0NTkxMF5BMl5BanBnXkFtZTcwMjQ4MzMzMw@@._V1_QL50_SY1000_CR0,0,674,1000_AL_.jpg",
                    "https://www.youtube.com/watch?v=niD-jahFURU")

idiots = media.Movie("3 Idiots",
                    "Two friends are searching for their long lost companion. They revisit their college days and recall the memories of their friend who inspired them to think differently, even as the rest of the world called them 'idiots'.",
                    "https://images-na.ssl-images-amazon.com/images/M/MV5BZWRlNDdkNzItMzhlZC00YTdmLWIwNjktYjY5NjQ1ZmQ3N2FkXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_QL50_SY1000_CR0,0,747,1000_AL_.jpg",
                    "https://www.youtube.com/watch?v=xvszmNXdM4w")

movies = [toy_story, dangal, raees, minions, ratatouille, idiots]
#fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
print(media.Movie.__module__)
