#!/usr/bin/python3
"""
Module Name: 5-text_indentation

Module Description:
This module contains only one function

Module Functions:
- print_square(size: str = "") -> None

Module Attributes:
- None
"""
def text_indentation(text: str = "")-> None:
    """
    This function receives a string `text` as input and formats it by adding a new line after every ".", "?" and ":" characters. 
    The first character of the new line will be indented by adding two spaces before it.
    
    Args:
    text (str): The input string that needs to be formatted.
    
    Returns:
    None
    
    Raises:
    TypeError: If the input `text` is not a string.
    
    Example:
    text_indentation("Hello World. How are you? I am fine.")
    Output:
    Hello World.
    How are you?
    I am fine.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    if len(text) > 0:
        print(text[0], end="")
    for i in range(1, len(text)):
        if text[i] in [".", "?", ":"]:
            print(text[i])
            print()
        else:
            if text[i - 1] in [".", "?", ":"]:
                continue
            print(text[i], end="")
    
        