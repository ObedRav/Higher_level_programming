#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

__name__ = "__main__"

argv = sys.argv
allowed_operators = {"+": add, "-": sub, "*": mul, "/": div}


if (len(argv) != 4):
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    sys.exit(1)
elif (not argv[2] in allowed_operators):
    print("Unknown operator. Available operators: +, -, * and /")
    sys.exit(1)

a = int(argv[1])
b = int(argv[3])

print(f"{a} {argv[2]} {b} = {allowed_operators.get(argv[2])(a, b)}")
