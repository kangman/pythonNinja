import csv

def read_movies():
    with open('film.csv', 'rb') as f:
        reader = csv.reader(f, delimiter=';')
        rows = [row for row in reader]
    return rows[0], rows[1:]
    
