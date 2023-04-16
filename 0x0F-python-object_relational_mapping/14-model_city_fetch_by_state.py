#!/usr/bin/python3
"""
This script lists all cities objects from the database hbtn_0e_6_usa
"""

from sys import argv
from sqlalchemy import create_engine
from model_city import City
from model_state import State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Create SQLAlchemy engine with provided credentials
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    # Create session maker object
    session_maker = sessionmaker(bind=engine)

    # Create session object
    session = session_maker()

    # Query cities and their corresponding states and print the results
    for city, state in session.query(City, State)\
                              .filter(City.state_id == State.id)\
                              .order_by(City.id):
        print(f"{state.name}: ({city.id}) {city.name}")
