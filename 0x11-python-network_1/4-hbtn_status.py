#!/usr/bin/python3
import requests
""" Python script that fetches https://intranet.hbtn.io/status
Used the package requests
)"""

if __name__ == '__main__':
    response = requests.get('https://intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type: {}'.format(type(response.text)))
    print('\t- content: {}'.format(response.content.decode('utf-8')))