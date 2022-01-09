#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL and
displays the value of the X-Request-Id variable found in the header
of the response."""
import sys
import urllib.request as imported

if __name__ == '__main__':
    request = imported.Request(sys.argv[1])
    with imported.urlopen(request) as response:
        headers = response.headers
        print(headers.get('X-Request-Id'))
