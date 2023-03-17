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
    username, password, database_name = sys.argv[1:4]

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
        # Creating a new instance
        new_state = State(name="Louisiana")
        session.add(new_state)

        # commit the transaction
        session.commit()

        # Print the results
        print(new_state.id)


if __name__ == "__main__":
    Solution()
