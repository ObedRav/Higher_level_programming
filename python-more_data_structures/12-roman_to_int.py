#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_numbers = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    roman_int = 0
    temp = ""
    for i in roman_string:
        if (temp == "I" and i != "I"):
            roman_int -= 2
        roman_int += roman_numbers.get(i)
        temp = i
    return roman_int
