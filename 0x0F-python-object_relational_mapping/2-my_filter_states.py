#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys


if __name__ == "__main__":
    # Retrieve command line arguments
    username, password, database, state_name = sys.argv[1:]

    # Connect to database
    with MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=database,
        port=3306,
    ) as conn:

        # Create cursor object
        cur = conn.cursor()

        # Execute query
        cur.execute(
            "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id ASC",
            (state_name,)
        )

        # Fetch and display results
        for row in cur.fetchall():
            print(row)

        # Close cursor and connection
        cur.close()
