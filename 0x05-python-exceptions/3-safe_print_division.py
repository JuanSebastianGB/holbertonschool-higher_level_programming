#!/usr/bin/python3
def safe_print_division(a, b):
    """Return divition of a with b"""
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("inside result: {}".format(result))
    return result
