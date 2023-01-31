#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    div = []
    value = 0
    for i in range(list_length):
        try:
            if isinstance(my_list_1[i] / my_list_2[i], float):
                value = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            value = 0
            continue
        except TypeError:
            print("wrong type")
            value = 0
            continue
        except IndexError:
            print("out of range")
            value = 0
            continue
        finally:
            div.append(value)
    return div
