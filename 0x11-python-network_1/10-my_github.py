#!/usr/bin/python3
"""
Python script that takes GitHub credentials (username and password)
and uses the GitHub API to display the id
"""
from sys import argv
import requests
from requests.auth import HTTPBasicAuth

if __name__ == '__main__':
    response = requests.get('https://api.github.com/users/{}'.format(argv[1]),
                            auth=HTTPBasicAuth(argv[1], argv[2])).json()
    print(response.get('id'))
