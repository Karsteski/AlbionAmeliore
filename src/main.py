#!/bin/python

from PySide6.QtWidgets import QApplication

from typing import Any

from ui.main_window import MainWindow

import file_data
import api_data

from items import *

FILENAME = "../data/ao-bin-dumps/formatted/items.txt"
# ITEM_INFO_FILENAME ="ao-bin-dumps/items.json"

item_strings = file_data.getFileKeyValueData(FILENAME)
item_data = file_data.stringsToItems(item_strings)

string_to_find = "riding horse"
found_thingies = file_data.findNearestItemNames(item_data, string_to_find)

items: list[Item] = []
for thingy in found_thingies:
    items.append([item for item in item_data if item.name == thingy][0])

# TODO: Need to add error handling and tests
response: list[dict[str, Any]]= api_data.getCurrentPrices(items,
                                [api_data.City.Lymhurst],
                                )
market_data: list[MarketData]= api_data.marketResponsetoMarketData(response)
# print(market_data)
# print(response)
# print(market_data[0].city.name)


# Do Qt stuff
if True :
    application = QApplication([])
    main_window = MainWindow()
    main_window.setMarketDataTableItem(market_data)
    main_window.show()
    application.exec()

