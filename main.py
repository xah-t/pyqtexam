import sys
from PySide2 import QtWidgets, QtCore, QtGui
import kalku


class KalkuWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = kalku.Ui_MainWindow()
        self.ui.setupUi(self)
        self.mykalku = MyKalku()

    def closeEvent(self, event: QtCore.QEvent.Close):
        reply = QtWidgets.QMessageBox.question(self, "Выход", "Вы действительно хотите выйти?")
        print(reply)
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
            print('Window closed')
        elif reply == QtWidgets.QMessageBox.No:
            event.ignore()
            print('Window not closed')

    def moveEvent(self, event: QtCore.QEvent.Move) -> None:
        reply = QtCore.QEvent.Move
        print("окно движется")



    def event(self, event: QtCore.QEvent) -> bool:
        print(event.type())
        if event.type() == QtCore.QEvent.Type.Close:
            event.setAccepted(False)
        return QtWidgets.QMainWindow.event(self, event)


class MyKalku(QtCore.QThread):
    pass


if __name__ == '__main__':

    app = QtWidgets.QApplication()
    widget = KalkuWindow()
    widget.show()
    app.exec_()
