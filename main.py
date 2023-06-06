import requests
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/chart/top'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
movies = soup.select('td.titleColumn')
ratings = soup.select('td.posterColumn span[name="ir"]')

movie_ratings = {}

for movie, rating in zip(movies, ratings):
    movie_title = movie.a.text
    movie_year = movie.span.text
    movie_rating = float(rating['data-value'])
    movie_ratings[movie_title + ' (' + movie_year + ')'] = movie_rating

# выводим список лучших 250 фильмов
top_movies = list(movie_ratings.items())[:250]

# выводим названия фильмов и их рейтинги
for movie, rating in top_movies:
    print(movie, rating)