from bvapi import bva_api
from credentials import *  # contains username en pass

api = bva_api(USERNAME, PASSWORD)  # from credentials
print(api.login())
