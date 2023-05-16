import json
import requests

from items import *

item_info = "T3_FARM_WHEAT_SEED?locations=&qualities=0"
"""

request = API_HOST_URL + ENDPOINT + item_info
response = requests.get(request)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Error:", response.status_code)
"""


def getCurrentPrices(items: list[Item], 
                     locations: list[Location],
                     qualities: Quality = Quality.Normal):
    pass
