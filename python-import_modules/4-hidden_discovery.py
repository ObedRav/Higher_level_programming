#!/usr/bin/python3
import dis
import hidden_4

# Get the bytecode for the module
bytecode = hidden_4.__code__.co_code

# Disassemble the bytecode
dis.dis(bytecode)

# Extract the names of the defined variables
names = [name for name in dis.get_names(bytecode) if not name.startswith("__")]

# Sort the names in alphabetical order
names.sort()

# Print each name on a new line
for name in names:
    print(name)
