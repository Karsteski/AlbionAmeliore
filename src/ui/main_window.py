from PySide6.QtWidgets import QMainWindow

from ui.ui_classes.ui_albionameliore import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
