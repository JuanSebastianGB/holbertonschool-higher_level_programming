#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """function that prints x elements of a list. using exception"""
    counter = 0
    for index in range(x):
        try:
            print("{}".format(my_list[index]), end="")
            counter += 1
        except IndexError:
            break
    print("")
    return counter
