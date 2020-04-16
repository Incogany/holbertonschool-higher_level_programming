#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL
and displays the body of the response.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    error = requests.get(url)
    if error.status_code == 200:
        print(error.text)
    else:
        print("Error code: {}".format(error.status_code))
