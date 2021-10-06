#!/usr/bin/python3
from typing import Type


def text_indentation(text):
    if type(text) is not str:
        raise TypeError("text must be a string")
    text = text.replace(".", ".\n\n").replace(
        "?", "?\n\n").replace(":", ":\n\n")
    print(text)
