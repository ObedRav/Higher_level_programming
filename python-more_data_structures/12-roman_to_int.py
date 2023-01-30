#!/usr/bin/python3
def roman_to_int(roman_string):
    if (not isinstance(roman_string, str) or roman_string is None):
        return 0
    roman_numbers = \
        {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    roman_int = 0
    temp = roman_string[0]
    for i in roman_string:
        if (roman_numbers.get(temp) < roman_numbers.get(i)):
            roman_int -= roman_numbers.get(temp) * 2
        roman_int += roman_numbers.get(i)
        temp = i
    return roman_int
