import csv, random

def read_movies():
    with open('film.csv', 'rb') as f:
        reader = csv.reader(f, delimiter=';')
        rows = [row for row in reader]
    return rows[0], rows[2:]

def get_short_movies(movies):
    """"
    Take the movies list and filter out those
    that are longer than 120 minutes.
    """
    short_movies = []
    for movie in movies:
        try:
            if int(movie[1]) < 120:
                short_movies.append(movie)
        except:
            continue
    return short_movies

def recommend_from(short_movies):
    return random.choice(short_movies)

def get_popular_movies(movies):
    popular_movies = []
    for movies in movies:
        try:
            if int(movie[7]) > 40:
                popular_movies.append(movie)
        except:
            continue
    return popular_movies

def netflix_me():
    """
    read in the movies
    filter just the short ones
    filter just the popular movies
    recommend one of those from the resultant list
    print out the name
    """
    headers, movies = read_movies()
    short_movies = get_short_movies(movies)
    popular_movies = get_popular_movies(short_movies)
    recommendation = recommend_from(short_movies)
    print recommendation[2]
