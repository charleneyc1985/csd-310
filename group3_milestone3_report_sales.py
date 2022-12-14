# Group 3
# Bryce Kellas, Andrew McCloud, Charlene Centeno, James Beck
# Module 10 - Milestone 3
#
# Script to generate equipment sales report for the Outland Adventures

import mysql.connector
from mysql.connector import errorcode
from datetime import date

def print_body(cursor):
    """ Query data for report, print to screen in formatted for readility """

    cursor.execute(""" 
    SELECT orders.productID, products.product_name, products.unit_cost, COUNT(orders.orderID) quantity, products.unit_cost * COUNT(orders.orderID)
    FROM orders
    INNER JOIN products
    ON orders.productID = products.productID
    GROUP BY orders.productID
    """)
    report_data = cursor.fetchall()  # List of tuples

    for row in report_data:
        print("{:<10s}{:<13s}\t{:<16s}{:>5d}\n{:<10s}{:>11.2f}\t{:<16s}{:>5d}\n{:<10s}{:>11.2f}"
            .format("Product:", row[1], "ID:", row[0], "Price:", row[2], "Sold Quantity:", row[3], "Total:", row[4]))
        print() # Blank line


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
report_title = "Equipment Sales"
print("{:<30s}{:>12s}".format(report_title, report_run_date.strftime("%m/%d/%Y")))

# Print the body of the report
print_body(cursor)

db.close()