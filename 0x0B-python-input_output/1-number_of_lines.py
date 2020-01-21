#!/usr/bin/python3
def number_of_lines(filename=""):
    """
    function that returns the number of lines of a text file
    """
    count = 0
    with open(filename, 'r') as f:
        while f.readline() is not '':
            count += 1
        return count
