import sys
from PySide2 import QtWidgets, QtCore
import kalku


class KalkuWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = kalku.Ui_MainWindow()
        self.ui.setupUi(self)
        self.mykalku = MyKalku()


class MyKalku(QtCore.QThread):
    pass


if __name__ == '__main__':

    app = QtWidgets.QApplication()
    widget = KalkuWindow()
    widget.show()
    app.exec_()