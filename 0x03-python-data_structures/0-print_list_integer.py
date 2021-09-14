#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """[function that prints all integers of a list.]

    Args:
        my_list (list, optional): [list of elements]. Defaults to [].
    """
    for element in my_list:
        print("{:d}".format(element))
