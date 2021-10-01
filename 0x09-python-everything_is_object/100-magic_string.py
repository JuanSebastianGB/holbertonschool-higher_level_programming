#!/usr/bin/python3
def magic_string():
    magic_string.string = getattr(magic_string, 'string', -1) + 1
    return "BestSchool, " * (magic_string.string) + "BestSchool"
