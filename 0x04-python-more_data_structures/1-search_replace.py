#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """replaces all occurrences of an element by another in a new list."""
    my_list = my_list[:]
    for index, value in enumerate(my_list):
        if search == value:
            my_list[index] = replace
    return my_list
