#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """deletes the item at a specific position in a list."""
    if idx >= 0 and len(my_list) >= idx + 1:
        del(my_list[idx])
    return my_list
