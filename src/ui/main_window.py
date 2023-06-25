from PySide6.QtGui import QAction, QKeySequence
from PySide6.QtWidgets import QMainWindow, QTableWidgetItem
from PySide6.QtCore import Qt

from ui.ui_classes.ui_albionameliore import Ui_MainWindow

from enum import Enum

import items

class ColumnHeader(Enum):
    Name = 0
    City = 1
    Lowest_Sell_Price = 2
    Highest_Sell_Price = 3
    Lowest_Buy_Price = 4
    Highest_Buy_Price = 5


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Menu
        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu("File")

        # Exit QAction 
        # self.exit_action = QAction("Exit", self)

        self.table_market_data = self.ui.tableMarketData


    # Market Data Table
    def setNumTableItems(self, number: int) -> None:
        self.table_market_data.setRowCount(number)

    def setMarketDataTableItem(self, marketData: list[items.MarketData]) -> None:
        self.table_market_data.setRowCount(len(marketData))

        for i, market_data in enumerate(marketData):
            self.table_market_data.setItem(i, ColumnHeader.Name.value, QTableWidgetItem(market_data.item.name))
            self.table_market_data.setItem(i, ColumnHeader.City.value, QTableWidgetItem(str(market_data.city)))
            self.table_market_data.setItem(i, ColumnHeader.Lowest_Sell_Price.value, QTableWidgetItem(str(market_data.min_sell_price)))
            self.table_market_data.setItem(i, ColumnHeader.Highest_Sell_Price.value, QTableWidgetItem(str(market_data.max_sell_price)))
            self.table_market_data.setItem(i, ColumnHeader.Lowest_Buy_Price.value, QTableWidgetItem(str(market_data.min_buy_price)))
            self.table_market_data.setItem(i, ColumnHeader.Highest_Buy_Price.value, QTableWidgetItem(str(market_data.max_buy_price)))
