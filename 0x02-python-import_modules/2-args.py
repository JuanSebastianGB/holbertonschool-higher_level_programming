#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    """Print a list the elements with the  correspondent number
    """
    lgth = len(argv) - 1
    if lgth == 0:
        print("0 arguments.")
    elif lgth == 1:
        print("1 argument:")
    else:
        print("{:d} arguments:".format(lgth))
    for i, s in enumerate(argv):
        if i > 0:
            print("{}: {}".format(i, s))
