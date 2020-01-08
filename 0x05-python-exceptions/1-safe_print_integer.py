#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if value == 0:
            print("{:d}".format(value))
            return True
        else:
            print("{:d}".format(value))
            return True
    except ValueError:
        return False
