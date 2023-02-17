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

    def to_json(self, attributes=None):
        """
        Serializes the instance attributes to a dictionary
        representation of JSON.

        Args:
            attributes (list): Optional list of attribute names
                               to include in the returned dictionary.
                               If not provided or None, all instance
                               attributes will be included.

        Returns:
            A dictionary representing the serialized JSON.
        """
        if attributes or attributes == []:
            dictionary = {}
            for key, value in self.__dict__.items():
                if key in attributes:
                    dictionary[key] = value
            return dictionary
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """
        Updates the instance attributes based on a JSON representation.

        Args:
            json (dict): A dictionary representing the JSON.

        Returns:
            None
        """
        keys_inicialization = list(self.__dict__.keys())
        for key, value in json.items():
            if key in keys_inicialization:
                self.__setattr__(key, value)
