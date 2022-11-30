// Charlene Centeno - CSD310 - Module 8 - 11/29/2022
// Insert, Update, Delete


import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="movies_user",
    password="popcorn",
    database="movies"
)

cursor = db.cursor()

def show_films(cursor, title):

    cursor.execute("SELECT film_name as Name, film_director as Director, genre_name as Genre, studio_name as 'Studio Name' \
                from film \
                 INNER JOIN genre ON film.genre_id=genre.genre_id \
                 INNER JOIN studio ON film.studio_id=studio.studio_id")

    films = cursor.fetchall()

    print("\n-- DISPLAYING FILMS --".formart(title))

    for film in films:
        print("Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n".format(film[0], film[1], film[2], film[3]))

def insert_film(cursor, title):

    cursor.execute("INSERT INTO film(film_name, film_director, studio_id, genre_id)")
    VALUES('Alien', 'George Lucas', (SELECT studio_id FROM studio WHERE studio_name = '20th Century Fox'),(SELECT genre_id FROM genre WHERE genre_name = 'SciFi') );

    db.commit()

    cursor.execute("SELECT film_name as Name, film_director as Director, genre_name as Genre, studio_name as 'Studio Name' \
                    from film \
                     INNER JOIN genre ON film.genre_id=genre.genre_id \
                     INNER JOIN studio ON film.studio_id=studio.studio_id")

    addedfilms = cursor.fetchall()

    print("\n-- DISPLAYING FILMS AFTER INSERT --")

    for addedfilm in addedfilms:
        print("Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n".format(addedfilm[0], addedfilm[1], addedfilm[2], addedfilm[3]))

def update_genre(cursor, title):

    cursor.execute("UPDATE genre SET genre_name = 'Horror' WHERE film_name = 'Alien'")

    db.commit()

    cursor.execute("SELECT film_name as Name, film_director as Director, genre_name as Genre, studio_name as 'Studio Name' \
                        from film \
                         INNER JOIN genre ON film.genre_id=genre.genre_id \
                         INNER JOIN studio ON film.studio_id=studio.studio_id")

    update = cursor.fetchall()

    print("\n-- DISPLAYING FILMS AFTER UPDATE- Changed Alien to Horror --")

    for update in updates:
        print("Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n".format(update[0], update[1],
                                                                                         update[2], update[3]))

def delete_film(cursor, title):

    cursor.execute("DELETE FROM film WHERE film_name = 'Gladiator'")

    db.commit()

    cursor.execute("SELECT film_name as Name, film_director as Director, genre_name as Genre, studio_name as 'Studio Name' \
                        from film \
                         INNER JOIN genre ON film.genre_id=genre.genre_id \
                         INNER JOIN studio ON film.studio_id=studio.studio_id")

    delete = cursor.fetchall()

    print("\n-- DISPLAYING FILMS AFTER DELETE --")

    for delete in deletes:
        print("Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n".format(delete[0], delete[1],
                                                                                         delete[2], delete[3]))

