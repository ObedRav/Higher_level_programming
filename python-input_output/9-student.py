#!/usr/bin/python3
"""
Module Name: 9-student

Module Description:
This module contains only one function

Module Classes:
- Student

Module Attributes:
- None
"""


class Student:
    """
    Represents a student with their first name, last name, and age.
    """
    def __init__(self, first_name: str, last_name: str, age: int):
        """
        Initializes the object with the given first_name, last_name, and age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Returns a dictionary containing the object's attributes as key-value
        pairs, where the keys are the attribute names and the values are the
        attribute values. This method is useful for JSON serialization
        of the object.
        """
        return self.__dict__
