from bvapi import bva_api
from credentials import *  # contains username en pass
from pprint import pprint

api = bva_api(USERNAME, PASSWORD)  # from credentials
pprint(api.login())

pprint(api.get_lot_by_number(43687, 12))
