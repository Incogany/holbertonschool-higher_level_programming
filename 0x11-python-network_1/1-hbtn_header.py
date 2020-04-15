#!/usr/bin/python3
# Python script that fetches https://intranet.hbtn.io/status
import urllib.request
import sys
if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        html = response.headers['X-Request-Id']
        print(html)
