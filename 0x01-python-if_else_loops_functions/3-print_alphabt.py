#!/usr/bin/python3
for n in range(0, 26):
    if n != 4 and n != 16:
        print("{:s}".format(chr(ord('a') + n)), end="")
