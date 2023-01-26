#!/usr/bin/python3


def is_negative(number):
    return number < 0


def remove_char_at(str, n):
    if (is_negative(n)):
        return str
    string = f"{str[:n]}{str[n+1:]}"
    return string
