#!/usr/bin/python3
# Python script that fetches https://intranet.hbtn.io/status
import requests
import sys

if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    html = response.headers['X-Request-Id']
    print(html)
