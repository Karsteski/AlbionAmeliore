#!/bin/python

from typing import Any, Final
import dataclasses
import json
import csv
import requests

import file_data
import api_data
import items

FILENAME = "../data/ao-bin-dumps/formatted/items.txt"
# ITEM_INFO_FILENAME ="ao-bin-dumps/items.json"

item_strings = file_data.getFileKeyValueData(FILENAME)
item_data = file_data.stringsToItems(item_strings)

print(api_data.getCurrentPrices([item_data[3]],
                                [api_data.City.Bridgewatch],
                                ))


