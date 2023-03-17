#!/usr/bin/python3

"""
Module Name: 14-model_city_fetch_by_state

Module Description:
This module contains only one function that prints all City objects from the
database that are related to a specific State object.

Module Functions:
- Solution() -> None

Module Attributes:
- None
"""

import sys

from model_state import State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def Solution():
    """
    Prints all City objects related to a
    specific State object from the database
    """
    try:
        # Destructure the args
        username, password, database_name = sys.argv[1:4]

        # Create a database connection
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
            username,
            password,
            database_name),
            pool_pre_ping=True)

        # Create a session factory
        Session = sessionmaker(bind=engine)

        # Use the with statement to handle the
        # session and connection automatically
        with Session() as session:
            for city, state in session.query(City, State) \
                              .filter(City.state_id == State.id) \
                              .order_by(City.id):
                print("{}: ({}) {}".format(state.name, city.id, city.name))

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    Solution()
