import sys
from PySide2 import QtWidgets, QtCore, QtGui, QtSql
import kalku


class KalkuWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        print('init')
        QtWidgets.QMainWindow.__init__(self, parent)
        self.mykalkul = MyKalkul()
        self.ui = kalku.Ui_MainWindow()
        self.ui.setupUi(self)
        #self.ui.lineEdit_6.setHidden(True)
        #self.ui.lineEdit_7.setHidden(True)
        #self.ui.lineEdit_8.setHidden(True)

        self.initSqlModel()
        self.ui.PBSaved.clicked.connect(self.onPBSaveclicked)
        self.ui.PBRaschet.clicked.connect(self.onPBRaschetclicked)
        self.ui.PBMoved.clicked.connect(self.onPBMoveclicked)
        self.mykalkul.signalTrudoemkost.connect(self.setLineEditTrudoemkost, QtCore.Qt.QueuedConnection)
        self.mykalkul.signalSebestoimost.connect(self.setLineEditSebestoimost, QtCore.Qt.QueuedConnection)
        self.mykalkul.signalVremyapartii.connect(self.setLineEditVremyaPartii, QtCore.Qt.QueuedConnection)

    def setLineEditTrudoemkost(self, text):
        self.ui.LETrudoemkost.setText(text)

    def setLineEditSebestoimost(self, text):
        self.ui.LESebestoimost.setText(text)

    def setLineEditVremyaPartii(self, text):
        self.ui.LEVremyapartii.setText(text)

    def initSqlModel(self):
        self.db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('C:/Users/nva10/Downloads/fieldlist_var2.db')  # C:/Users/nva10/Downloads/fieldlist_var2.db
        self.model = QtSql.QSqlTableModel()
        self.model.setTable('fieldlist')

        self.model.select()  # подключение БД
        # инициализация БД(создание)
        self.model.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, "Наименование")
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, "Децимальный №")
        self.model.setHeaderData(3, QtCore.Qt.Horizontal, "Площадь, мм2")
        self.model.setHeaderData(4, QtCore.Qt.Horizontal, "Глубина, мм")
        self.model.setHeaderData(5, QtCore.Qt.Horizontal, "Трудоемкость, н/ч")
        self.model.setHeaderData(6, QtCore.Qt.Horizontal, "Стоимость, руб. с НДС")  # заменить на стоимость изделия(сложить трудоемкость и материал)
        self.model.setHeaderData(7, QtCore.Qt.Horizontal, "Срок изготовления, час")  # не отображается в окне

        self.ui.tableView.setModel(self.model)
        self.ui.tableView.setColumnHidden(0, True)  # скрытие столбцов
        self.ui.tableView.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

    def onPBRaschetclicked(self):
        self.mykalkul.setParameters(self.ui.LENaimenovanie.text(),
                                    self.ui.LEArticul.text(),
                                    self.ui.LEKolichestvo.text(),
                                    self.ui.LEPloshad.text(),
                                    self.ui.LEGlubina.text())
        self.mykalkul.start()
        print('onPBRaschetclicked')

    def onPBSaveclicked(self):
        index = self.model.rowCount()
        self.model.insertRows(index, 1)
        self.model.setData(self.model.index(index, 1), self.ui.LENaimenovanie.text())
        self.model.setData(self.model.index(index, 2), self.ui.LEArticul.text())
        #self.model.setData(self.model.index(index, 3), self.ui.lineEdit_3.text())
        self.model.setData(self.model.index(index, 3), self.ui.LEPloshad.text())
        self.model.setData(self.model.index(index, 4), self.ui.LEGlubina.text())
        self.model.setData(self.model.index(index, 5), self.ui.LETrudoemkost.text())
        self.model.setData(self.model.index(index, 6), self.ui.LESebestoimost.text())
        self.model.setData(self.model.index(index, 7), self.ui.LEVremyapartii.text())
        self.model.submitAll()

        print('onPBSaveclicked')

    def onPBMoveclicked(self):
        if self.ui.tableView.currentIndex().row() > -1:

            index_list = []
            for model_index in self.ui.tableView.selectionModel().selectedRows():
                index = QtCore.QPersistentModelIndex(model_index)
                index_list.append(index)

            for index in index_list:
                 self.model.removeRow(index.row())
        else:
            QtWidgets.QMessageBox.about(self, 'Message', 'Выберите строку')
        print("onPBMoveClicked")

    def setLineEdit_4Text(self, text):
        self.lineEdit_4.setText(text)

    def closeEvent(self, event: QtCore.QEvent.Close):
        reply = QtWidgets.QMessageBox.question(self, "Выход", "Вы действительно хотите выйти?")
        print(reply)
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
            print('Window closed')
        elif reply == QtWidgets.QMessageBox.No:
            event.ignore()
            print('Window not closed')


    def event(self, event: QtCore.QEvent) -> bool:
        #print(event.type())
        if event.type() == QtCore.QEvent.Type.Close:
            event.setAccepted(False)
        return QtWidgets.QMainWindow.event(self, event)


class MyKalkul(QtCore.QThread):
    signalTrudoemkost = QtCore.Signal(str)
    signalSebestoimost = QtCore.Signal(str)
    signalVremyapartii = QtCore.Signal(str)

    def __init__(self, parent=None):
        super(MyKalkul, self).__init__(parent)

    def setParameters(self, naimenovanie, artikul, kolichestvo, ploshad, glubina):

        self.naimenovanie = naimenovanie
        self.artikul = artikul
        self.kolichestvo = kolichestvo
        self.ploshad = ploshad
        self.glubina = glubina

    def run(self):
        print(self.naimenovanie)
        print(self.artikul)
        print(self.kolichestvo)
        print(self.ploshad)
        print(self.glubina)
        skorost = int(self.ploshad) * 1.8  # 1.8 - стандартное время обработки 1мм2
        skorostsloev = int(self.glubina) * skorost  # кол-во слоев * Nмм2/сек
        resultTrud = skorostsloev / 3600  # трудоемкость = площадь обработки*кол-во секунт / 3600(перевод в н/ч)
        resultSebest = resultTrud * 2350  # в дальнейшем - вписать ссылку на lineEdit с ценой нормочаса
        vremyapartii = skorostsloev * int(self.kolichestvo) / 3600
        print(f"Трудоёмкость {resultTrud}")
        print(f"Себестоимость {resultSebest}")
        print(f"Время обработки партии {vremyapartii} часов")

        self.signalTrudoemkost.emit(str(resultTrud))
        self.signalSebestoimost.emit(str(resultSebest))
        self.signalVremyapartii.emit(str(vremyapartii))


"""
#Пример создания дочернего окна из основной формы


import sys
 
from PyQt4 import QtGui, QtCore
 
 
class SecondWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        # Передаём ссылку на родительский элемент и чтобы виджет
        # отображался как самостоятельное окно указываем тип окна
        super().__init__(parent, QtCore.Qt.Window)
        self.build()
 
    def build(self):
        self.mainLayout = QtGui.QVBoxLayout()
 
        self.buttons = []
        for i in range(5):
            but = QtGui.QPushButton('button {}'.format(i), self)
            self.mainLayout.addWidget(but)
            self.buttons.append(but)
 
        self.setLayout(self.mainLayout)
 
 
class MainWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.secondWin = None
        self.build()
 
    def build(self):
        self.mainLayout = QtGui.QVBoxLayout()
 
        self.lab = QtGui.QLabel('simple text', self)
        self.mainLayout.addWidget(self.lab)
 
        self.but1 = QtGui.QPushButton('open window', self)
        self.but1.clicked.connect(self.openWin)
        self.mainLayout.addWidget(self.but1)
 
        self.setLayout(self.mainLayout)
 
    def openWin(self):
        if not self.secondWin:
            self.secondWin = SecondWindow(self)
        self.secondWin.show()
 
 
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
"""

if __name__ == '__main__':

    app = QtWidgets.QApplication()
    widget = KalkuWindow()
    widget.show()
    app.exec_()
