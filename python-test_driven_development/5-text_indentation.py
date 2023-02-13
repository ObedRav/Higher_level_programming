#!/usr/bin/python3
"""
Module Name: 5-text_indentation

Module Description:
This module contains only one function

Module Functions:
- def text_indentation(text) -> None

Module Attributes:
- None
"""


def text_indentation(text) -> None:
    """
    This function takes a string `text` as input and adds new line characters after each sentence,
    ending with `.`, `?` or `:`.

    Input:
    text: A string representing the text to be indented.

    Output:
    None. The function outputs the indented text directly to the console.

    Exceptions Raised:
    TypeError: If `text` is not a string.

    Example:
    >>> text_indentation("Example text. Second line. Third line?")
    Example text.
    <BLANKLINE>
    Second line.
    <BLANKLINE>
    Third line?
    <BLANKLINE>
    """
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
