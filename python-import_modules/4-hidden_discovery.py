#!/usr/bin/python3
import hidden_4

__name__ = "__main__"

# Extract the names of the defined variables
names = [name for name in dir(hidden_4) if not name.startswith("__")]

# Sort the names in alphabetical order
names.sort()

# Print each name on a new line
for name in names:
    print(name)
