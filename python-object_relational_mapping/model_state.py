#!/usr/bin/python3
"""
Module Name: model_state

Module Description:
This module contains only one class

Classes:
- State

Module Attributes:
- None
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """State class that inherits from Base.

    Attributes:
        __tablename__ (str): The name of the table in the database.
        id (int): The unique identifier for the state.
        name (str): The name of the state.
    """
    __tablename__ = "states"
    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
