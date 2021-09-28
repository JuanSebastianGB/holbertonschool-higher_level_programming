#!/usr/bin/python3
def safe_print_integer(value):
    """prints an integer with "{:d}".format(). using ValueError exception"""
    try:
        print("{:d}".format(value))
        return True
    except ValueError:
        return False
