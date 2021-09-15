#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """prints a dictionary by ordered keys."""
    for el in sorted(a_dictionary):
        print("{}: {}".format(el, a_dictionary[el]))
