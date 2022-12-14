# Group 3
# Bryce Kellas, Andrew McCloud, Charlene Centeno, James Beck
# Module 10 - Milestone 3
#
# Script to generate trips report for the Outland Adventures

import mysql.connector
from mysql.connector import errorcode
from datetime import date

def print_trips(cursor):
    """ Query data for report, print to screen in formatted for readility """

    cursor.execute(""" 
    SELECT locations.locationID as ID, locations.location_name as Location, COUNT(trips.locationID) as Quantity
    FROM locations
    INNER JOIN trips
    ON locations.locationID = trips.locationID
    GROUP BY locations.locationID
    """)
    report_trips = cursor.fetchall()  # List of tuples

    for trip in report_trips:
        print("ID: {}\nLocation: {}\nQuantity: {}\n".format(trip[0], trip[1], trip[2]))


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
report_run_date = date.today()

# Print Report title with today's date
report_title = "Trip Trends"
print("{:<30s}{:>12s}".format(report_title, report_run_date.strftime("%m/%d/%Y")))

# Print the body of the report
print_trips(cursor)

db.close()