#!/usr/bin/python3
"""Defining the locked Class"""


class LockedClass:
    """prevents the user from dynamically creating new instance"""

    __slots__ = ["first_name"]
