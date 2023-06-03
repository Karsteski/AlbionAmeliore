#!/bin/python

from typing import Any
import sys

from PySide6.QtWidgets import QApplication
from PySide6.QtQuick import QQuickView



import file_data
import api_data
from items import *

FILENAME = "../data/ao-bin-dumps/formatted/items.txt"
# ITEM_INFO_FILENAME ="ao-bin-dumps/items.json"

item_strings = file_data.getFileKeyValueData(FILENAME)
item_data = file_data.stringsToItems(item_strings)



string_to_find = "quaterstaff"
found_thingies = file_data.findNearestItemNames(item_data, string_to_find)

items: list[Item] = []
for thingy in found_thingies:
    items.append([item for item in item_data if item.name == thingy][0])

# response : list[dict[str, Any]]= api_data.getCurrentPrices(items,
#                                 [api_data.City.Lymhurst],
#                                 )
# lol :list[MarketData]= api_data.marketResponsetoMarketData(response)
#

app = QApplication()
view = QQuickView()

view.setSource("qml/view.qml")
view.show()
sys.exit(app.exec())

