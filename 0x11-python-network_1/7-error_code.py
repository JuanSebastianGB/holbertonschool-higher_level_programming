#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL
and displays the body of the response.

If the HTTP status code is greater than or equal to 400, print:
Error code: followed by the value of the HTTP status code
"""
import sys
import requests
import requests.exceptions as exceptions

if __name__ == '__main__':
    response = requests.get(sys.argv[1])
    code = response.status_code
    if code > 299:
        print('Error code: {}'.format(code))
    else:
        print(response.text)
