#!/usr/bin/python3
def no_c(my_string):
    """function that removes all characters c and C from a string."""
    new_string = [elem for elem in my_string if elem != 'C' and elem != 'c']
    return("".join(new_string))
