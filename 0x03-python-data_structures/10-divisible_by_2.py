#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """finds all multiples of 2 in a list."""
    copy = my_list[:]
    return [True if element % 2 == 0 else False for element in my_list]
