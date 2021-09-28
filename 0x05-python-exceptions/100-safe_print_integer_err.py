#!/usr/bin/python3
def safe_print_integer_err(value):
    """prints an integer."""
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError) as errors:
        from sys import stderr
        print("Exception: {}".format(errors))
        return False
    else:
        return True
