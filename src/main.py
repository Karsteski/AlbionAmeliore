#!/bin/python

from PySide6.QtWidgets import QApplication

from PySide6.QtCore import QFile, QIODeviceBase
from PySide6.QtWidgets import QMainWindow
from PySide6.QtUiTools import QUiLoader

from typing import Any
import sys

import file_data
import api_data
import ui.main_window

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
                                # [api_data.City.Lymhurst],
                                # )
# lol :list[MarketData]= api_data.marketResponsetoMarketData(response)


application = QApplication([])


qUiLoader = QUiLoader()

path = ""
file = QFile("/home/karsteski/dev/albionameliore/src/ui/ui_files/albionameliore.ui")
file.open(QIODeviceBase.OpenModeFlag.ReadOnly)

albion_ameliore = qUiLoader.load(file, None)
albion_ameliore.show()

# main_window = ui.main_window.MainWindow()
# main_window.show()

application.exec()
