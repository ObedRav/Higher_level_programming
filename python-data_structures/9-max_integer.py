#!/usr/bin/python3
def max_integer(my_list=[]):
    my_list.sort()
    return_value = my_list[-1] if my_list else None
    return return_value
