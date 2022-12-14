# Group 3
# Bryce Kellas, Andrew McCloud, Charlene Centeno, James Beck
# Module 10 - Milestone 3
#
# Script to generate inventory report for the Outland Adventures. Displays only products that have been in inventory more than five years.

import mysql.connector
from mysql.connector import errorcode
from datetime import date

def print_products(cursor):
    """ Query data for report, print to screen in formatted for readility. EDIT-BKellas: ORDER BY Age in Years to bring 
    the oldest items to the top of the report. """

    cursor.execute("""
    SELECT productID as ID, product_name as Product, manufacturer_name as Manufacturer, 
    inventory_date as Stocked, TIMESTAMPDIFF(YEAR, inventory_date, CURDATE()) as 'Age in Years'
    FROM products
    ORDER BY TIMESTAMPDIFF(YEAR, inventory_date, CURDATE()) DESC
    """)

    report_inventory = cursor.fetchall()  # List of tuples

    for product in report_inventory:
        print("ID: {}\nProduct: {}\nManufacturer: {}\nStocked: {}\nAge in Years: {}\n".format(product[0], product[1], product[2], product[3], product[4]))


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
report_title = "Product Inventory"
print("{:<30s}{:>12s}".format(report_title, report_run_date.strftime("%m/%d/%Y")))

# Print the body of the report
print_products(cursor)

db.close()