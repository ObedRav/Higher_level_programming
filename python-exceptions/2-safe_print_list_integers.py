#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    numbers_printing = 0
    try:
        for i in range(x):
            print("{:d}".format(my_list[i]), end="")
            numbers_printing += 1
        if (x > i):
            raise IndexError("list index out of range")
    finally:
        print()
        return numbers_printing
