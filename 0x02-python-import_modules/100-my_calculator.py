#!/usr/bin/python3
if __name__ == "__main__":
    """[Using imported modules of calculator and implementing some validations]
    """
    from calculator_1 import add, sub, mul, div
    import sys

    argv = sys.argv
    operations = {
        "+": add,
        "-": sub,
        "*": mul,
        "/": div
    }
    if len(argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(argv[1])
    b = int(argv[3])
    if argv[2] not in list(operations.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    print("{} {} {} = {}".format(a, argv[2], b, operations[argv[2]](a, b)))
