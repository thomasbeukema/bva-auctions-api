# Author: Thomas Beukema <thomasbeukema@outlook.com>
# This file is licensed under the MIT License. Please see LICENSE for more details.
import requests

"""
    bva_api

    bva_api is an API wrapper for the BVA Auction API,
    which can be found at https://api-acc.bva-auctions.com/api/docs/.
"""


class bva_api:

    # Base URL for every API call
    base_url = "https://api-acc.bva-auctions.com/api/rest/"
    base_url_no_acc = "https://api.bva-auctions.com/api/rest/"
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
    # returns True when successful, otherwise returns error msg
    def login(self):
        # set json body
        data = {
            'username': self.username,
            'password': self.password
        }
        url = self.base_url + 'tokenlogin'
        response = requests.post(url, json=data, headers=self.request_headers)

        if response.status_code == 201:  # 201 equals success
            body = response.json()

            # extract everything
            self.first_name = body['firstName']
            self.language = body['language']
            self.email = body['email']

            self.request_headers['accessToken'] = body['accessToken']
            self.request_headers['refreshToken'] = body['refreshToken']
            self.request_headers['X-CSRF-Token'] = body['csrfToken']

            return True  # success
        else:
            return response.json()['message']  # failed

    # logout deletes tokens from server
    def logout(self):
        url = self.base_url + 'logout'
        response = requests.post(url, headers=self.request_headers)
        if not response.ok:
            return response.json()['message']
        return True

    # get_auction retrieves auction details
    # @param auction_id: the id of the auction
    def get_auction(self, auction_id):
        url = self.base_url + 'ext123/auction/{}'.format(auction_id)
        response = requests.get(url, headers=self.request_headers)

        if response.ok:
            return response.json()
        else:
            return response.json()['message']

    # get_auction_categories retrieves the (sub)category
    # of the auction
    # @param auction_id: the id of the auction
    def get_auction_categories(self, auction_id):
        url = self.base_url_no_acc + \
            'ext123/auction/{}/nl/lotcategories/true/true'.format(auction_id)
        response = requests.get(url, headers=self.request_headers)

        print(url)

        if response.ok:
            return response.text
        else:
            return response.json()['message']

    # get_auction_locations retrieves the locations
    # of the auction, 'Online' if delivered at home
    # @param auction_id: the id of the auction
    def get_auction_locations(self, auction_id):
        url = self.base_url + 'ext123/auction/{}/locations'.format(auction_id)
        response = requests.get(url, headers=self.request_headers)

        if response.ok:
            return response.json()
        else:
            return response.json()['message']

    # get_lot_by_number retrieves a lot with lot_id
    # @param lot: the id of the lot
    def get_lot(self, lot_id):
        url = self.base_url_no_acc + 'ext123/lot/{}'.format(lot_id)
        response = requests.get(url, headers=self.request_headers)

        if response.ok:
            return response.json()
        else:
            return response.json()['message']

    # get_lot_by_number retrieves a lot with auction_id and lot_number
    # @param auction_id: the id of the auction
    # @param lot: the id of the lot
    # @param lot: additional to lot id, defaults to ''
    def get_lot_by_number(self, auction_id, lot_number, lot_number_addition=''):
        url = self.base_url_no_acc + \
            'ext123/lot/{}/{}{}/lotbynumber'.format(
                auction_id, lot_number, lot_number_addition)
        response = requests.get(url, headers=self.request_headers)

        if response.ok:
            return response.json()
        else:
            return response.json()['message']

    # search searches for given term
    def search(self, term, additional_query=''):
        url = self.base_url_no_acc + \
            'search?term={}{}'.format(term, additional_query)
        response = requests.get(url, headers=self.request_headers)

        if response.ok:
            return response.json()
        else:
            return response.json()['message']

    # get_invoices retrieves a list of invoices
    def get_invoices(self, limit=20, page_index=1):
        url = self.base_url + \
            '/ext123/invoices?limit={}&pageNumber={}'.format(limit, page_index)

        response = requests.get(url, headers=self.request_headers)

        if response.ok:
            return response.json()
        else:
            return response.json()['message']

    # get_from_invoice lets you retrieve certain data by invoice
    def get_from_invoice(self, invoice_id, pdf=True, status=False, payment_url=False):
        toReturn = []

        if pdf:
            url = self.base_url + \
                'ext123/invoices/{}/pdf'.format(invoice_id)
            response = requests.get(url, headers=self.request_headers)

            print(url)

            if response.ok:
                toReturn.append(response.text)
            else:
                toReturn.append([False, response.json()])

        if status:
            url = self.base_url + \
                'invoices/{}/status'.format(invoice_id)
            response = requests.get(url, headers=self.request_headers)

            if response.ok:
                toReturn.append(response.json())
            else:
                toReturn.append([False, response.json()])

        if payment_url:
            url = self.base_url + \
                'ext123/invoices/{}/paymenturl'.format(invoice_id)
            response = requests.get(url, headers=self.request_headers)

            if response.ok:
                toReturn.append(response.json())
            else:
                print(response.json())
                toReturn.append([False, response.json()])

        return toReturn
