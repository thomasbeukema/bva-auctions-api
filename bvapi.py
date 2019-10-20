# Author: Thomas Beukema <thomasbeukema@outlook.com>
# This file is licensed under the MIT License. Please see LICENSE for more details.
import requests


class bva_api:

    # Base URL for every API call
    base_url = "https://api-acc.bva-auctions.com/api/rest/"
    # Headers to include with every request
    request_headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'User-Agent': 'BVA API'
    }
    first_name = ''
    language = ''
    email = ''

    def __init__(self, username, password, user_agent='BVA API'):
        self.username = username
        self.password = password
        self.request_headers['User-Agent'] = user_agent

    # login fetches tokens needed for protected endpoints
    # returns True when successful, otherwise returns False
    def login(self):
        # set json body
        data = {
            'username': self.username,
            'password': self.password
        }
        url = self.base_url + 'tokenlogin'
        response = requests.post(url, json=data)

        if response.status_code == 201:  # 201 equals success
            body = response.json()

            # extract everything
            self.first_name = body['firstName']
            self.language = body['language']
            self.email = body['email']

            self.request_headers['accessToken'] = body['accessToken']
            self.request_headers['refreshToken'] = body['refreshToken']
            self.request_headers['X-CSRF-Token'] = body['csrfToken']

            return True
        else:
            return False
