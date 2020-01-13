#!/usr/bin/python3
"""
Function that print the fist and last name
and vaidate if the variable is a string
Return: none
"""


def say_my_name(first_name, last_name=""):
    """Print The first and last name"""
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("{} {}".format(first_name, last_name))
