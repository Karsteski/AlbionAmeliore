from PySide6.QtGui import QAction, QKeySequence
from PySide6.QtWidgets import QMainWindow, QTableWidgetItem

from ui.ui_classes.ui_albionameliore import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Menu
        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu("File")

        # Exit QAction 
        self.exit_action = QAction("Exit", self)

        # Status Bar
        self.ui.statusbar.setWindowIconText("lol")
    
