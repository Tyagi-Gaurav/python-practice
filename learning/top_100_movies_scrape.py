from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
page = response.text
soup = BeautifulSoup(page, "html.parser")

all_movies = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__BfenH")
all_movies = reversed(all_movies)
movie_list = [movie.get_text() for movie in all_movies]
movie_text = "\n".join(movie_list)

with open("movies.txt", "w") as file:
    file.write(movie_text)
