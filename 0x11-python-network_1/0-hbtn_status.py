#!/usr/bin/python3
"""Python script that fetches https://intranet.hbtn.io/status"""
import urllib.request as imported

if __name__ == '__main__':

    with imported.urlopen('https://intranet.hbtn.io/status') as response:
        content = response.read()
        print('Body response:')
        print('    - type: {}'.format(type(content)))
        print('    - content: {}'.format(content))
        print('    - utf8 content: {}'.format(content.decode('utf-8')))
