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

    def __init__(self, username, password, user_agent):
        self.username = username
        self.password = password
        self.request_headers['User-Agent'] = user_agent

    def login(self):
        data = {
            'username': self.username,
            'password': self.password
        }
