moviereviews = []

class movieRe:
    def __init__(self,movie,story,actors,music):
        self.moviename=movie

        self.storyrating=story
        self.actorsrating=actors
        self.musicrating=music
        

        self.avg = int((self.storyrating + self.actorsrating + self.musicrating)/3)

        self.myrating ={
        "movie" :self.moviename,
        "story_r" :self.storyrating,
        "actors_r" :self.actorsrating,
        "music_r" :self.musicrating,
        "avg_r" :self.avg
        }
    def add_movie_rating(self,movie_list):
        movie_list.append(self.myrating)

    def avg_star_rating(self, movie_list):
        for i in movie_list:
            if(i["avg_r"]==1):
                print("Thanks for the Review, you gave the movie *")
                print(i)

            elif(i["avg_r"]==2):
                print("Thanks for the Review, you gave the movie * *")
                print(i)

            elif(i["avg_r"]==3):
                print("Thanks for the Review, you gave the movie * * *")
                print(i)

            elif(i["avg_r"]==4):
                print("Thanks for the Review, you gave the movie * * * *")
                print(i)

            if(i["avg_r"]==5):
                print("Thanks for the Review, you gave the movie * * * * *")
                print(i)

            

review1 = movieRe("Frozen", 1, 1, 3)

review1.add_movie_rating(moviereviews)
review1.avg_star_rating(moviereviews)


