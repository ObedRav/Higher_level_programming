#!/usr/bin/python3
def multiple_returns(sentence):
    if (not sentence):
        return None
    length = len(sentence)
    last_digit = (sentence[0])
    return length, last_digit
