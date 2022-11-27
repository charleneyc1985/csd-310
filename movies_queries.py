import mysql.connector

config = {
    "user": "root",
    "password": "popcorn",
    "host": "localhost",
    "database": "movies",
}
db = mysql.connector.connect(**config)
cursor = db.cursor()

cursor.execute("SELECT studio_id, studio_name FROM studio")

studio = cursor.fetchall()

print('\n-- DISPLAYING Studio RECORDS --')

for studio in studio:
    print("Studio ID: {} \nStudio Name: {}".format(studio[0], studio[1]))
    print()

cursor.execute("SELECT genre_id, genre_name FROM genre")

genre = cursor.fetchall()

print('\n-- DISPLAYING Genre RECORDS --')

for genre in genre:
    print("Genre ID: {} \nGenre Name: {}".format(genre[0], genre[1]))
    print()

cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime < 120")

film = cursor.fetchall()

print('\n-- DISPLAYING Short Film RECORDS --')

for film in film:
    print("Film Name: {} \nRuntime: {}".format(film[0], film[1]))
    print()

cursor.execute("SELECT film_name, film_director FROM film ORDER BY film_director")

film = cursor.fetchall()

print('\n-- DISPLAYING Director RECORDS in Order --')

for film in film:
    print("Film Name: {} \nDirector: {}".format(film[0], film[1]))
    print()
