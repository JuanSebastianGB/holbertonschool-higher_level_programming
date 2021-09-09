#!/usr/bin/python3
def magic_calculation(a, b):
    """[Emulating the output in assembly required]

    Args:
        a ([int]): [number 1]
        b ([int]): [number 2]

    Returns:
        [int]: [result]
    """
    from magic_calculation_102 import add, sub
    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return c
    else:
        return (sub(a, b))
