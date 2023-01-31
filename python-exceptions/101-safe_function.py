#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        x = fct(*args)
        return x
    except ZeroDivisionError as err:
        print(f"Exception: {err.args[0]}", file=sys.stderr)
    except IndexError as err1:
        print(f"Exception: {err1.args[0]}", file=sys.stderr)
