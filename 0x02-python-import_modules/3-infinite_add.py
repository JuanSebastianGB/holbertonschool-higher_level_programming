#!/usr/bin/python3
if __name__ == "__main__":
    """[Implemeting infinite addition of all input arguments]
    """
    import sys
    arguments = sys.argv
    sum = 0
    for number, value in enumerate(arguments):
        if number > 0:
            sum += int(value)
    print("{}".format(sum))
