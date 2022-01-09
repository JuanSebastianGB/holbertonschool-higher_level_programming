#!/usr/bin/python3
"""Python script that takes in a URL and an email, sends a POST
request to the passed URL with the email as a parameter, and displays
the body of the response (decoded in utf-8)"""

import urllib.request as request
import urllib.parse as parse
import sys

data = parse.urlencode({"email": sys.argv[2]}).encode("ascii")
if __name__ == '__main__':
    req = request.Request(sys.argv[1], data)
    with request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
