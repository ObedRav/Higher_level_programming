#!/usr/bin/python3
for number in range(100):
    if (number == 99):
        print("{}".format(number))
    else:
        print("{}, ".format(str(number).zfill(2)), end="")
