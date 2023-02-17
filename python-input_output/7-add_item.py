#!/usr/bin/python3
"""
Script for adding command-line arguments to a list stored in a JSON file.

Usage:
./7-add_item arg1 arg2 arg3 ...


The script reads the current list from the "add_item.json"
file, and appends the given command-line arguments to the list.
If the file does not exist, it will be created with an empty list.
The updated list is then written back to the file.

Functions:
    - load_from_json_file(filename): Reads a JSON file and returns
                                     the Python object it represents.
    - save_to_json_file(my_obj, filename):
                        Writes a Python object to a JSON file.

Arguments:
    - filename: The name of the JSON file to read/write.
    - my_obj: The Python object to be written to the JSON file.

Exceptions:
    - FileNotFoundError: Raised when the specified file cannot be found.

Example:
    - Suppose the "add_item.json" file contains the list [1, 2, 3].
    The command "python3 add_item.py 4 5 6" will append the arguments
    to the list, resulting in [1, 2, 3, "4", "5", "6"].

"""
import sys

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

try:
    json_data = load_from_json_file("add_item.json")
except FileNotFoundError:
    with open("add_item.json", "w") as f:
        f.write("[]")
    exit(0)

for argv_data in sys.argv[1:]:
    json_data.append(argv_data)
save_to_json_file(json_data, "add_item.json")
