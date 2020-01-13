#!/usr/bin/python3
"""
Function that print the fist and last name a square
Return: none
"""


def print_square(size):
    """Print the square with the caracter #"""

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
