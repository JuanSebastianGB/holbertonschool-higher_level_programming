#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    longitud = len(argv) - 1
    print("{:d}".format(longitud))
    for i in range(1, longitud + 1):
        print("{:d}: {:s}".format(i, argv[i]))
