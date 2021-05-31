import sys
from PySide2 import QtWidgets, QtCore, QtGui, QtSql
import kalku


class KalkuWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = kalku.Ui_MainWindow()
        self.ui.setupUi(self)
        #self.ui.lineEdit_6.setHidden(True)
        #self.ui.lineEdit_7.setHidden(True)
        #self.ui.lineEdit_8.setHidden(True)
        self.mykalku = MyKalku()
        self.initSqlModel()

    def initSqlModel(self):
        self.db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('fiedlist.db')
        self.model = QtSql.QSqlTableModel()
        self.model.setTable('field')
        self.model.select() # подключение БД
        # инициализация БД(создание)
        self.model.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, "Наименованеие")
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, "Децимальный №")
        self.model.setHeaderData(3, QtCore.Qt.Horizontal, "Площадь, мм2")
        self.model.setHeaderData(4, QtCore.Qt.Horizontal, "Глубина, мм")
        self.model.setHeaderData(5, QtCore.Qt.Horizontal, "Трудоёмкость н/ч")
        self.model.setHeaderData(6, QtCore.Qt.Horizontal, "Себестоимость, руб.")

        self.ui.tableView.setModel(self.model)
        self.ui.tableView.setColumnHidden(0, True) # скрытие столбцов
        self.ui.tableView.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

    def closeEvent(self, event: QtCore.QEvent.Close):
        reply = QtWidgets.QMessageBox.question(self, "Выход", "Вы действительно хотите выйти?")
        print(reply)
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
            print('Window closed')
        elif reply == QtWidgets.QMessageBox.No:
            event.ignore()
            print('Window not closed')

    # def moveEvent(self, event: QtCore.QEvent.Move) -> None:
    #     reply = QtCore.QEvent.Move
    #     print(event.pos())

    def event(self, event: QtCore.QEvent) -> bool:
        #print(event.type())
        if event.type() == QtCore.QEvent.Type.Close:
            event.setAccepted(False)
        return QtWidgets.QMainWindow.event(self, event)


class MyKalku(QtCore.QThread):

    def layuot_speed():
        pass
    pass

if __name__ == '__main__':

    app = QtWidgets.QApplication()
    widget = KalkuWindow()
    widget.show()
    app.exec_()
