import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
empire_online_webpage = response.text

soup = BeautifulSoup(empire_online_webpage, "html.parser")
movie_tags = soup.find_all(name="h3", class_="title")
movie_titles = [movie.get_text() for movie in movie_tags]
movie_titles.reverse()

with open('movies.txt', 'w', encoding="utf-8") as data_file:
    for movie in movie_titles:
        data_file.write(f"{movie}\n")

print(movie_titles)


