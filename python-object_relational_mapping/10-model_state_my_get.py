#!/usr/bin/python3
"""
Module Name: 7-model_state_fetch_all

Module Description:
This module contains only one function

Module Functions:
- Solution() -> None

Module Attributes:
- None
"""
import sys

from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def Solution():
    """Prints all State objects that contain the letter a from the database."""
    # Desestructuring the args
    username, password, database_name, state_name = sys.argv[1:5]

    # Creating database connection
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        username,
        password,
        database_name),
        pool_pre_ping=True)

    # Create a session factory
    Session = sessionmaker(bind=engine)

    # Use the with to handle the close session
    with Session() as session:
        # Query the database for all states
        states = \
            session.query(State).filter_by(name=state_name)

        # Print the results
        if states is None or states.count() == 0:
            print("Not found")
        else:
            for state in states.all():
                print(state.id)


if __name__ == "__main__":
    Solution()
