#!/usr/bin/python3
def weight_average(my_list=[]):
    """returns the weighted average of all integers tuple"""
    if len(my_list) == 0:
        return 0

    return sum([pair[1] * pair[0] for pair in my_list])\
        / sum([pair[1] for pair in my_list])
