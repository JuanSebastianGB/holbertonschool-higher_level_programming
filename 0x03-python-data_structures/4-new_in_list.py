#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """replaces an element in a list at a specific position
    without modifying the original list (like in C)."""
    copy = my_list[:]
    if idx >= 0 or idx + 1 <= len(my_list):
        copy[idx] = element
    return copy
