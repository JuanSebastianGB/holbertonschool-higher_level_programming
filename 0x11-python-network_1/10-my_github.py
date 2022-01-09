#!/usr/bin/python3
"""
Python script that takes GitHub credentials (username and password)
and uses the GitHub API to display the id
"""
from sys import argv
import requests

if __name__ == '__main__':
    auth = (argv[1], argv[2])
    response = requests.get('https://api.github.com/user', auth=auth).json()
    print(response.get('id'))
