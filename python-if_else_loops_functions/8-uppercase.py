#!/usr/bin/python3
def uppercase(string):
    for i in range(len(string)):
        if ord(string[i]) >= 97 and ord(string[i]) <= 122:
            print("{}".format(chr(ord(string[i]) - 32)), end='')
        else:
            print("{}".format(string[i]), end='')
