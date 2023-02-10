#!/usr/bin/python3
"""This code test itself"""


def text_indentation(text):
    """This function print a new line if the text == .?:"""
    i = 0
    if type(text) != str:
        raise TypeError('text must be a string')
    while i < len(text):
        print(text[i], end="")
        if text[i] == "\n" or text[i] in ".?:":
            if text[i] in ".?:":
                print("\n")
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1
