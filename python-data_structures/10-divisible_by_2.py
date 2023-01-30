#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    divisible_by_2 = []
    for number in my_list:
        if (number % 2) == 0:
            divisible_by_2.append(True)
        else:
            divisible_by_2.append(False)
    return divisible_by_2
