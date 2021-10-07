#!/usr/bin/python3
""" Definition of the function text_indentation """


def text_indentation(text):
    """[ prints a text with 2 new lines after each of these characters:
    ., ? and :]

    Args:
        text ([str]): [text - string to process]

    Raises:
        TypeError: [if not is a string]
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    text = text.replace(".", ".\n\n").replace(
        "?", "?\n\n").replace(":", ":\n\n")
    text = "\n".join([row.lstrip(" ").rstrip(" ") for row in text.split("\n")])
    print(text, end="")
