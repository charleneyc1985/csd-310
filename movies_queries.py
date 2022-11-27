# Charlene Centeno - 11/26/2022 - Module 7
# Movies: Table Queries
# The first and second query is to select all the fields for the studio and genre tables.
# The third query is to select the movie names for those movies that have a run time of less than two hours.
# The fourth query is to get a list of film names, and directors grouped by director.

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="popcorn",
    database="movies"
)

mycursor = mydb.cursor()

# select all the fields for the studio tables

mycursor.execute("SELECT studio_id, studio_name FROM studio")

studio = mycursor.fetchall()

print('\n-- DISPLAYING Studio RECORDS --')

for studio in studio:
    print("Studio ID: {} \nStudio Name: {}".format(studio[0], studio[1]))
    print()

# select all the fields for the genre tables
    
mycursor.execute("SELECT genre_id, genre_name FROM genre")

genre = mycursor.fetchall()

print('\n-- DISPLAYING Genre RECORDS --')

for genre in genre:
    print("Genre ID: {} \nGenre Name: {}".format(genre[0], genre[1]))
    print()

# select the movie names for those movies that have a run time of less than two hours
    
mycursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime < 120")

film = mycursor.fetchall()

print('\n-- DISPLAYING Short Film RECORDS --')

for film in film:
    print("Film Name: {} \nRuntime: {}".format(film[0], film[1]))
    print()

# select a list of film names, and directors grouped by director
    
mycursor.execute("SELECT film_name, film_director FROM film ORDER BY film_director")

film = mycursor.fetchall()

print('\n-- DISPLAYING Director RECORDS in Order --')

for film in film:
    print("Film Name: {} \nDirector: {}".format(film[0], film[1]))
    print()
