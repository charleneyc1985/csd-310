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

# drop tables if they are present
cursor.execute("DROP TABLE IF EXISTS orders")
cursor.execute("DROP TABLE IF EXISTS rentals")
cursor.execute("DROP TABLE IF EXISTS products")
cursor.execute("DROP TABLE IF EXISTS inventory")

cursor.execute("DROP TABLE IF EXISTS customers")
cursor.execute("DROP TABLE IF EXISTS trips")
cursor.execute("DROP TABLE IF EXISTS employees")
cursor.execute("DROP TABLE IF EXISTS locations")


# Initialize tables
# Inventory
cursor.execute("""CREATE TABLE inventory (
    inventoryID             INT             NOT NULL                     AUTO_INCREMENT,
    product_quantity        VARCHAR(75)     NOT NULL,
    inventory_location      VARCHAR(20)     NOT NULL,
    
    PRIMARY KEY(inventoryID)
    ) 
""")

# Products
cursor.execute("""CREATE TABLE products (
    productID               INT             NOT NULL        AUTO_INCREMENT,
    product_name            VARCHAR(50)     NOT NULL,
    unit_cost               DEC(5, 2)       NOT NULL,
    manufacturer_name       VARCHAR(50)     NOT NULL,
    inventoryID             INT             NOT NULL,
    rental_cost             DEC(5,2),
            
    PRIMARY KEY(productID),

    CONSTRAINT fk_inventory
    FOREIGN KEY(inventoryID)
        REFERENCES inventory(inventoryID)
    )
""")

# Locations
cursor.execute("""CREATE TABLE locations (
    locationID               INT             NOT NULL        AUTO_INCREMENT,
    location_name            VARCHAR(50)     NOT NULL,
                    
    PRIMARY KEY(locationID)
    )
""")

# Employees
cursor.execute("""CREATE TABLE employees (
    employeeID               INT              NOT NULL        AUTO_INCREMENT,
    employee_name            VARCHAR(50)      NOT NULL,
    department               VARCHAR(20)      NOT NULL,

    PRIMARY KEY(employeeID)
    )
""")

# Trips
cursor.execute("""CREATE TABLE trips (
    tripID                  INT            NOT NULL        AUTO_INCREMENT,
    employeeID              INT            NOT NULL,
    locationID              INT            NOT NULL,
    airport                 VARCHAR(50)    NOT NULL,
    airfare                 DEC(7, 2)      NOT NULL,
    depart_date             DATE           NOT NULL,
    return_date             DATE           NOT NULL,
    inoculations            BOOLEAN        NOT NULL,

    PRIMARY KEY(tripID),

    CONSTRAINT fk_employees
    FOREIGN KEY(employeeID)
        REFERENCES employees(employeeID),

    CONSTRAINT fk_locations
    FOREIGN KEY(locationID)
        REFERENCES locations(locationID)
    )
""")

# Customers
cursor.execute("""CREATE TABLE customers (
    customerID               INT             NOT NULL        AUTO_INCREMENT,
    customer_name            VARCHAR(50)     NOT NULL,
    address                  VARCHAR(50)      NOT NULL,
    city                     VARCHAR(50)     NOT NULL,
    state                    VARCHAR(75)     NOT NULL,
    zip_code                 INT             NOT NULL,
    email                    VARCHAR(50)     NOT NULL,
    phone_number             VARCHAR(10)     NOT NULL,
    tripID                   INT,            

    PRIMARY KEY(customerID),

    CONSTRAINT fk_trips
    FOREIGN KEY(tripID)
        REFERENCES trips(tripID)
    )
""")

# Orders
cursor.execute("""CREATE TABLE orders (
    orderID               INT             NOT NULL        AUTO_INCREMENT,
    customerID            INT             NOT NULL,
    order_date            DATE            NOT NULL,
    order_total           DEC(5, 2)       NOT NULL,
    productID             INT             NOT NULL,
    rental                BOOLEAN         NOT NULL,
    rent_start_date       DATE,
    rent_end_date         DATE,
    rental_total          DEC(5, 2),
            
    PRIMARY KEY(orderID),

    CONSTRAINT fk_products
    FOREIGN KEY(productID)
        REFERENCES products(productID)
    )
""")


# Insert values
# Inventory
print(1)
cursor.execute("""INSERT INTO inventory (product_quantity, inventory_location)
    VALUES (12,"aisle 1"),
    (10,"aisle 2"),
    (7,"aisle 3"),
    (28,"aisle 4"),
    (15,"aisle 5"),
    (20,"aisle 6")
""")
db.commit()

# Products
print(2)
cursor.execute("""INSERT INTO products (product_name, unit_cost, manufacturer_name, inventoryID, rental_cost)                          
    VALUES ("Small Tent", 24.99, "Coleman", 1,19),
    ("Medium Tent",49.99,"Coleman",2,37),
    ("Large Tent",74.99,"Hilleberg",3,56),
    ("Day Pack",49.99,"Port Authority",4,37),
    ("Backpack",99.99,"Topo Designs",5,75),
    ("Camping Pot",19.99,"GSI Outdoors",6,15)
""")
db.commit()

# Locations
print(3)
cursor.execute("""INSERT INTO locations (location_name)
    VALUES ("Africa"),
    ("Asia"),
    ("Southern Europe")
""")
db.commit()

# Employees
print(4)
cursor.execute("""INSERT INTO employees (employee_name, department)
    VALUES ("Blythe Timmerson","Owners"),
    ("Jim Ford","Owners"),
    ("John MacNell","Guide"),
    ("D.B. Marland","Guide"),
    ("Anita Gallegos","Marketing"),
    ("Dimitrios Stravopolous","Supplies"),
    ("Mei Wong","Developer/Designer")
""")
db.commit()

# Trips
print(5)
cursor.execute("""INSERT INTO trips (employeeID, locationID, airport, airfare, depart_date, return_date, inoculations)
    VALUES (3,1,"Los Angeles International",809,'2023-01-25','2023-01-30',TRUE),
    (3,2,"Bradley International Airport",1322,'2023-02-18','2023-02-25',TRUE),
    (4,1,"Brunswick Golden Isles Airport",1012,'2023-03-04','2023-03-08',TRUE),
    (3,3,"Baltimore Washington International Airport",987,'2023-03-11','2023-03-18',TRUE),
    (4,3,"LaGuardia Airport",1100,'2023-03-29','2023-04-06',TRUE),
    (4,1,"Laredo International Airport",1289,'2023-04-19','2023-04-26',TRUE)
""")
db.commit()

# Customers
print(6)
cursor.execute("""INSERT INTO customers (customer_name, address, city, state, zip_code, email, phone_number, tripID)
VALUES ("Mirabel Madrigal","42 Wallaby Way","Redondo Beach","CA",57489,"mmad@yahoo.net","3283295834",6),
    ("Arya Stark","88 Direwolf Ave","Windsor Locks","CT",43593,"starka@hotmail.uk","1383842794",4),
    ("Finn Balor","128 Prince St","Brunswick","GA",49534,"dino@gmail.com","4359834998",2),
    ("Seth Rollins","438 Coffee Ln","Baltimore","MA",56843,"caffeine@me.com","3459834891",5),
    ("Becky Lynch","89 Pumpkin Dr","Queens","NY",43838,"toast@yum.com","3243848391",1),
    ("Wednesday Addams","13 Hummingbird","Laredo","TX",34939,"thing@gmail.com","2342394923",3)
""")
db.commit()

# Orders
print(7)
cursor.execute("""INSERT INTO orders (productID, customerID, order_date, order_total, rental, rent_start_date, rent_end_date, rental_total)
    VALUES (4,3,'2022-11-21',49.99,TRUE,'2023-02-18','2023-02-25',19),
    (6,5,'2022-12-02',19.99,FALSE,NULL,NULL,37),
    (4,5,'2022-12-05',49.99,FALSE,NULL,NULL,56),
    (5,1,'2022-12-06',99.99,TRUE,'2023-01-25','2023-01-30',37),
    (3,4,'2022-12-12',74.99,FALSE,NULL,NULL,75),
    (3,2,'2022-12-15',74.99,FALSE,NULL,NULL,15)
""")
db.commit()

print("done")
db.close()
