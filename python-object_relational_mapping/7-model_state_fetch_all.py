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
    """Prints all the states from the database."""
    # Creating database connection
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]),
        pool_pre_ping=True)

    # Create a session factory
    Session = sessionmaker(bind=engine)

    # Use the with to handle the close session
    with Session() as session:
        # Query the database for all states
        states = session.query(State).all()

        # Print the results
        for state in states:
            print(f"{state.id}: {state.name}")


if __name__ == "__main__":
    Solution()
