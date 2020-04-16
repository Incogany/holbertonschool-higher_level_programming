#!/usr/bin/python3
"""
Python script that takes your Github credentials
(username and password) and uses the Github API to display your id
"""

import sys
import requests
if __name__ == "__main__":
    url = 'https://api.github.com/user'

    user = sys.argv[1]
    token = sys.argv[2]
    response = requests.get(url, auth=(user, token))
    info = response.json()
    try:
        print(info['id'])
    except KeyError:
        print('None')
