from bvapi import bva_api
from credentials import *  # contains username en pass
from pprint import pprint

api = bva_api(USERNAME, PASSWORD)  # from credentials
pprint(api.login())

pprint(api.search('sieraad'))
