#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """prints all integers of a list, in reverse order."""
    if isinstance(my_list, list):
        for element in my_list[::-1]:
            print("{:d}".format(element))
