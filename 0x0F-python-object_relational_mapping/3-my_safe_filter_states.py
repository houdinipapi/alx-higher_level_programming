#!/usr/bin/python3
"""
This script queries the 'states' table in a MySQL database
for rows with a given state name.
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    # Connect to MySQL database using command line arguments
    conn = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])

    # Create cursor object
    cur = conn.cursor()

    # Execute SQL query with parameterized state name
    # to avoid SQL injection attacks
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC",
                (argv[4],))

    # Fetch and display query results
    [print(state) for state in cur.fetchall()]
