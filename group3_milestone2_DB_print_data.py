# Group 3
# Bryce Kellas, Andrew McCloud, Charlene Centeno, James Beck
# Module 9 - Milestone 2
#
# Script to initialize the Outland Adventures database and populate tables with 6 records.

import mysql.connector
from mysql.connector import errorcode


config = {
    "user": "OADB_user",
    "password": "popcorn",
    "host": "127.0.0.1",
    "database": "OutlandAdv",
    "raise_on_warnings": False
}


try:
    db = mysql.connector.connect(**config)

    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"],config["host"],config["database"]))

    input("\n\n Press enter to continue...")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

cursor = db.cursor()

# Display tables
# Inventory
cursor.execute("""SELECT * FROM inventory""") 
inventory = cursor.fetchall()
for item in inventory:
    print(item)

# Products
cursor.execute("""SELECT * FROM products""")
products = cursor.fetchall()
for item in products:
    print(item)

# Locations
cursor.execute("""SELECT * FROM locations""")
locations = cursor.fetchall()
for item in locations:
    print(item)

# Employees
cursor.execute("""SELECT * FROM employees""")
employees = cursor.fetchall()
for item in employees:
    print(item)

# Trips
cursor.execute("""SELECT * FROM trips""")
trips = cursor.fetchall()
for item in trips:
    print(item)

# Customers
cursor.execute("""SELECT * FROM customers""")
customers = cursor.fetchall()
for item in customers:
    print(item)

# Orders
cursor.execute("""SELECT * FROM orders""")
orders = cursor.fetchall()
for item in orders:
    print(item)

db.close()