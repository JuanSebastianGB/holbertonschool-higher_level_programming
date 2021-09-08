#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    longitud = len(argv) - 1
    print("{:d} arguments:".format(longitud))
    for i, s in enumerate(argv):
        if i > 0:
            print("{:d}: {:s}".format(i, s))
