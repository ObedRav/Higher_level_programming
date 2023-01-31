#!/usr/bin/python3
from itertools import zip_longest as zl


def list_division(my_list_1, my_list_2, list_length):
    div = []
    for list_1, list_2 in zl(my_list_1, my_list_2, fillvalue=None):
        try:
            if (list_1 is None or list_2 is None):
                raise ValueError
            if isinstance(list_1 / list_2, float):
                div.append(list_1 / list_2)
        except ZeroDivisionError:
            print("division by 0")
            div.append(0)
            continue
        except TypeError:
            print("wrong type")
            div.append(0)
            continue
        except ValueError:
            print("out of range")
            div.append(0)
            continue
    return div
