#!/usr/bin/python3
"""Module that containt append_after function"""


def append_after(filename="", search_string="", new_string=""):
    """[Function that nserts a line of text to a file, after each line
    containing a specific string]

    Args:
        filename (str, optional): [Name oof the file to override].
        Defaults to "".
        search_string (str, optional): [string to search]. Defaults to "".
        new_string (str, optional): [strin to add]. Defaults to "".
    """
    new_content = ""
    # Opening file
    with open(filename, mode="r") as f:
        for line in f:
            new_content += line
            if search_string not in line:
                new_content += new_string
    # overrinding mode
    with open(filename, mode="w", encoding="utf-8") as s:
        s.write(new_content)
