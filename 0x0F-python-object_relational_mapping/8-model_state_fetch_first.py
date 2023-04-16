#!/usr/bin/python3
"""
This script prints the first State object from the database hbtn_0e_6_usa
"""

from sys import argv
from sqlalchemy import create_engine
from model_state import State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Connect to MySQL database using provided credentials
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    # Create a session maker object to handle database connections
    session_maker = sessionmaker(bind=engine)

    # Create a new session object
    session = session_maker()

    # Query the State table for the first State object
    state = session.query(State).order_by(State.id).first()

    # Print the State object's id and name, or "Nothing" if no State is found
    print("Nothing" if state is None else f"{state.id}: {state.name}")
