#!/usr/bin/python3
def roman_to_int(roman_string):
    """converts a Roman numeral to an integer."""
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    romans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 100}
    result = 0
    for index, c in enumerate(roman_string):
        if c not in romans.keys():
            return 0
        if index < len(roman_string) - 1 and romans[roman_string[index]] < romans[roman_string[index + 1]]:
            result -= romans[roman_string[index]]
        else:
            result += romans[roman_string[index]]
    return result
