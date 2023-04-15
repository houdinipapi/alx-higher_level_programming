#!/usr/bin/python3

"""
lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ = "__main__":
    # Retrieve arguments
    mysql_username = sys.argv[1]
    mysql.password = sys.argv[2]
    database_name = sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=mysql_username,
                        passwd=mysql_password, db=database_name)

    # Create cursor object
    cursor = db.cursor()

    # Execute SQL query
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all rows
    rows = cursor.fetchall()

    # Display results
    for row in rows:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()
