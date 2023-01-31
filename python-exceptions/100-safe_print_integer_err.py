#!/usr/bin/python3
from sys import stderr as tderr


def safe_print_integer_err(value):
    string = "Exception: Unknown format code 'd'"
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        tderr.write(f"{string} for object of type 'str'\n")
        return False
