#!/usr/bin/python3

""" Module of the MyInt that inherits form object int """


class MyInt(int):
    """ MyInt has == and != operators inverted """

    def __eq__(self, x: object) -> bool:
        """ Operation equal interpreted like not equal"""
        return self.real != x

    def __ne__(self, x: object) -> bool:
        """ Operation Not equal interpreted like equal"""
        return self.real == x
