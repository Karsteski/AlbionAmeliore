#!/bin/python

from typing import Any, Final
import dataclasses
import json
import csv
import requests

import file_data

FILENAME = "../data/ao-bin-dumps/formatted/items.txt"
# ITEM_INFO_FILENAME ="ao-bin-dumps/items.json"
# API_HOST_URL = "https://west.albion-online-data.com"
# ENDPOINT = "/api/v2/stats/prices/"

item_strings = file_data.getFileKeyValueData(FILENAME)
items = file_data.stringsToItems(item_strings)

