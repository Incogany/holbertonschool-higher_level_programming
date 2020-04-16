#!/usr/bin/python3
"""
Python script that fetches https://intranet.hbtn.io/status
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    html = response.headers['X-Request-Id']
    print(html)
