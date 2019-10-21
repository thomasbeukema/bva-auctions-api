from bvapi import bva_api
from credentials import *  # contains username en pass
from pprint import pprint

api = bva_api(USERNAME, PASSWORD)  # from credentials
pprint(api.login())

pprint(api.get_from_invoice(69342008, pdf=True, status=True, payment_url=True))
