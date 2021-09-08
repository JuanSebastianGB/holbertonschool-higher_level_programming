#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    lgth = len(argv) - 1
    print("{:d} {:s}{:s}".format(
        lgth, "arguments" if lgth > 2 else "argument",
        "." if lgth == 1 else ":"))
    for i, s in enumerate(argv):
        if i > 0:
            print("{:d}: {:s}".format(i, s))
