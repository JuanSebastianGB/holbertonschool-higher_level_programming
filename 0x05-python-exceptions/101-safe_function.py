#!/usr/bin/python3
def safe_function(fct, *args):
    """ executes a function safely."""
    try:
        result = fct(*args)
        return result
    except:
        from sys import stderr, exc_info
        print("Exception: {}".format(exc_info()[1]), file=stderr)
        return None
