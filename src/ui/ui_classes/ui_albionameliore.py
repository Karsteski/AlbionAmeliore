# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'albionameliore.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTabWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1438, 608)
        self.centralWidget = QWidget(MainWindow)
        self.centralWidget.setObjectName(u"centralWidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.mainTabWidget = QTabWidget(self.centralWidget)
        self.mainTabWidget.setObjectName(u"mainTabWidget")
        self.mainTabWidget.setTabPosition(QTabWidget.North)
        self.tabMarketData = QWidget()
        self.tabMarketData.setObjectName(u"tabMarketData")
        self.verticalLayout = QVBoxLayout(self.tabMarketData)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frameMarketDataSearch = QFrame(self.tabMarketData)
        self.frameMarketDataSearch.setObjectName(u"frameMarketDataSearch")
        self.frameMarketDataSearch.setFrameShape(QFrame.StyledPanel)
        self.frameMarketDataSearch.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frameMarketDataSearch)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineMarketDataSearch = QLineEdit(self.frameMarketDataSearch)
        self.lineMarketDataSearch.setObjectName(u"lineMarketDataSearch")
        self.lineMarketDataSearch.setAutoFillBackground(False)

        self.horizontalLayout.addWidget(self.lineMarketDataSearch)

        self.frameMarketDataSearchButtons = QFrame(self.frameMarketDataSearch)
        self.frameMarketDataSearchButtons.setObjectName(u"frameMarketDataSearchButtons")
        self.frameMarketDataSearchButtons.setFrameShape(QFrame.NoFrame)
        self.frameMarketDataSearchButtons.setFrameShadow(QFrame.Plain)
        self.frameMarketDataSearchButtons.setLineWidth(0)
        self.horizontalLayout_3 = QHBoxLayout(self.frameMarketDataSearchButtons)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btnMarketDataBrecilien = QPushButton(self.frameMarketDataSearchButtons)
        self.btnMarketDataBrecilien.setObjectName(u"btnMarketDataBrecilien")
        self.btnMarketDataBrecilien.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.btnMarketDataBrecilien)

        self.lineMarketDataSearchButtons1 = QFrame(self.frameMarketDataSearchButtons)
        self.lineMarketDataSearchButtons1.setObjectName(u"lineMarketDataSearchButtons1")
        self.lineMarketDataSearchButtons1.setFrameShape(QFrame.VLine)
        self.lineMarketDataSearchButtons1.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.lineMarketDataSearchButtons1)

        self.btnMarketDataBridgewatch = QPushButton(self.frameMarketDataSearchButtons)
        self.btnMarketDataBridgewatch.setObjectName(u"btnMarketDataBridgewatch")
        self.btnMarketDataBridgewatch.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.btnMarketDataBridgewatch)

        self.btnMarketDataCaerleon = QPushButton(self.frameMarketDataSearchButtons)
        self.btnMarketDataCaerleon.setObjectName(u"btnMarketDataCaerleon")
        self.btnMarketDataCaerleon.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.btnMarketDataCaerleon)

        self.btnMarketDataFortSterling = QPushButton(self.frameMarketDataSearchButtons)
        self.btnMarketDataFortSterling.setObjectName(u"btnMarketDataFortSterling")
        self.btnMarketDataFortSterling.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.btnMarketDataFortSterling)

        self.btnMarketDataLymhurst = QPushButton(self.frameMarketDataSearchButtons)
        self.btnMarketDataLymhurst.setObjectName(u"btnMarketDataLymhurst")
        self.btnMarketDataLymhurst.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.btnMarketDataLymhurst)

        self.btnMarketDataMartlock = QPushButton(self.frameMarketDataSearchButtons)
        self.btnMarketDataMartlock.setObjectName(u"btnMarketDataMartlock")
        self.btnMarketDataMartlock.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.btnMarketDataMartlock)

        self.btnMarketDataThetford = QPushButton(self.frameMarketDataSearchButtons)
        self.btnMarketDataThetford.setObjectName(u"btnMarketDataThetford")
        self.btnMarketDataThetford.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.btnMarketDataThetford)

        self.lineMarketDataSearchButtons2 = QFrame(self.frameMarketDataSearchButtons)
        self.lineMarketDataSearchButtons2.setObjectName(u"lineMarketDataSearchButtons2")
        self.lineMarketDataSearchButtons2.setFrameShape(QFrame.VLine)
        self.lineMarketDataSearchButtons2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.lineMarketDataSearchButtons2)

        self.btnMarketDataArthursRest = QPushButton(self.frameMarketDataSearchButtons)
        self.btnMarketDataArthursRest.setObjectName(u"btnMarketDataArthursRest")
        self.btnMarketDataArthursRest.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.btnMarketDataArthursRest)

        self.btnMarketDataMerlynsRest = QPushButton(self.frameMarketDataSearchButtons)
        self.btnMarketDataMerlynsRest.setObjectName(u"btnMarketDataMerlynsRest")
        self.btnMarketDataMerlynsRest.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.btnMarketDataMerlynsRest)

        self.btnMarketDataMorganasRest = QPushButton(self.frameMarketDataSearchButtons)
        self.btnMarketDataMorganasRest.setObjectName(u"btnMarketDataMorganasRest")
        self.btnMarketDataMorganasRest.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.btnMarketDataMorganasRest)


        self.horizontalLayout.addWidget(self.frameMarketDataSearchButtons)


        self.verticalLayout.addWidget(self.frameMarketDataSearch)

        self.tableMarketData = QTableWidget(self.tabMarketData)
        if (self.tableMarketData.columnCount() < 6):
            self.tableMarketData.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableMarketData.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableMarketData.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableMarketData.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableMarketData.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableMarketData.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableMarketData.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        if (self.tableMarketData.rowCount() < 10):
            self.tableMarketData.setRowCount(10)
        self.tableMarketData.setObjectName(u"tableMarketData")
        self.tableMarketData.setMinimumSize(QSize(1406, 407))
        self.tableMarketData.setFrameShape(QFrame.StyledPanel)
        self.tableMarketData.setWordWrap(False)
        self.tableMarketData.setRowCount(10)
        self.tableMarketData.setColumnCount(6)
        self.tableMarketData.horizontalHeader().setVisible(True)
        self.tableMarketData.horizontalHeader().setCascadingSectionResizes(True)
        self.tableMarketData.horizontalHeader().setMinimumSectionSize(200)
        self.tableMarketData.horizontalHeader().setDefaultSectionSize(200)
        self.tableMarketData.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableMarketData.horizontalHeader().setStretchLastSection(False)
        self.tableMarketData.verticalHeader().setCascadingSectionResizes(False)
        self.tableMarketData.verticalHeader().setMinimumSectionSize(24)
        self.tableMarketData.verticalHeader().setDefaultSectionSize(24)
        self.tableMarketData.verticalHeader().setStretchLastSection(False)

        self.verticalLayout.addWidget(self.tableMarketData)

        self.mainTabWidget.addTab(self.tabMarketData, "")

        self.verticalLayout_2.addWidget(self.mainTabWidget)

        MainWindow.setCentralWidget(self.centralWidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1438, 28))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.mainTabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lineMarketDataSearch.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search...", None))
        self.btnMarketDataBrecilien.setText(QCoreApplication.translate("MainWindow", u"Brecilien", None))
        self.btnMarketDataBridgewatch.setText(QCoreApplication.translate("MainWindow", u"Bridgewatch", None))
        self.btnMarketDataCaerleon.setText(QCoreApplication.translate("MainWindow", u"Caerleon", None))
        self.btnMarketDataFortSterling.setText(QCoreApplication.translate("MainWindow", u"Fort Sterling", None))
        self.btnMarketDataLymhurst.setText(QCoreApplication.translate("MainWindow", u"Lymhurst", None))
        self.btnMarketDataMartlock.setText(QCoreApplication.translate("MainWindow", u"Martlock", None))
        self.btnMarketDataThetford.setText(QCoreApplication.translate("MainWindow", u"Thetford", None))
        self.btnMarketDataArthursRest.setText(QCoreApplication.translate("MainWindow", u"Arthur's Rest", None))
        self.btnMarketDataMerlynsRest.setText(QCoreApplication.translate("MainWindow", u"Merlyn's Rest", None))
        self.btnMarketDataMorganasRest.setText(QCoreApplication.translate("MainWindow", u"Morgana's Rest", None))
        ___qtablewidgetitem = self.tableMarketData.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem1 = self.tableMarketData.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"City", None));
        ___qtablewidgetitem2 = self.tableMarketData.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Lowest Sell Price", None));
        ___qtablewidgetitem3 = self.tableMarketData.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Highest Sell Price", None));
        ___qtablewidgetitem4 = self.tableMarketData.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Lowest Buy Price", None));
        ___qtablewidgetitem5 = self.tableMarketData.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Highest Buy Price", None));
        self.mainTabWidget.setTabText(self.mainTabWidget.indexOf(self.tabMarketData), QCoreApplication.translate("MainWindow", u"Market Data", None))
    # retranslateUi

