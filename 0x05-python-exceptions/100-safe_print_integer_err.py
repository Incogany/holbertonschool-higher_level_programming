#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
        return True
    except ValueError:
        sys.stderr.write("Exception: Unknown format code 'd' for object of ")
        sys.stderr.write("type 'str'\n")
        return False
    except TypeError:
        sys.stderr.write("TypeError: non-empty format string passed to ")
        sys.stderr.write("object.__format__\n")
        return False
