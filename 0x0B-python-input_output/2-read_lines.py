#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    """
    function that reads n lines of a text file (UTF8) and prints it to stdout
    """
    count = 0
    with open(filename, 'r') as f:
        while True:
            rd = f.readline()
            if rd is '':
                break
            print("{}".format(rd), end="")
            count += 1
            if count == nb_lines:
                break
