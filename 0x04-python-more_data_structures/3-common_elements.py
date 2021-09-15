#!/usr/bin/python3
def common_elements(set_1, set_2):
    """returns a set of common elements in two sets."""
    listado = []
    for el in set_1:
        if el in set_2:
            listado.append(el)
    return listado
