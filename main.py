import sys
from PySide2 import QtWidgets, QtCore, QtGui, QtSql
#import kalku
import kalkulation_window
import kalkulation_core
#import temp
#import temp
from xlsx_Extractor import Extractor


class KalkulationWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        print('init')
        QtWidgets.QMainWindow.__init__(self, parent)
        self.mykalkul = kalkulation_core.MyKalkulationCore()
        self.ui = kalkulation_window.Ui_MainWindow()  # kalku
        self.ui.setupUi(self)
        #self.ui.lineEdit_6.setHidden(True)
        #self.ui.lineEdit_7.setHidden(True)
        #self.ui.lineEdit_8.setHidden(True)

        self.initSqlModel()
        self.ui.PBSaved.clicked.connect(self.onPBSaveclicked)
        self.ui.PBRaschet.clicked.connect(self.onPBRaschetclicked)
        self.ui.PBMoved.clicked.connect(self.onPBMoveclicked)
        self.ui.PBExtract.clicked.connect(self.onPBExtractclicked)
        self.mykalkul.signalTrudoemkost.connect(self.setLineEditTrudoemkost, QtCore.Qt.QueuedConnection)
        self.mykalkul.signalSebestoimost.connect(self.setLineEditSebestoimost, QtCore.Qt.QueuedConnection)
        self.mykalkul.signalVremyapartii.connect(self.setLineEditVremyaPartii, QtCore.Qt.QueuedConnection)

    def setLineEditTrudoemkost(self, text):
        self.ui.LETrudoemkost.setText(text)

    def setLineEditSebestoimost(self, text):
        self.ui.LESebestoimost.setText(text)

    def setLineEditVremyaPartii(self, text):
        self.ui.LEVremyapartii.setText(text)

    # def setLineEditPloshad(self, text):
    #     self.ui.LEPloshad.setText(text)  # lineEdit_4

    def initSqlModel(self):
        self.db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('fieldlist_var2.db')  # 'fieldlist_var2.db'
        self.model = QtSql.QSqlTableModel()

        """ где то здесь прописать в переменную Джоин двух таблиц и ввести переменную как аргумент setTable"""
        self.model.setTable('fieldlist')  # название таблицы fieldlist, а не БД
        # self.model1 = QtSql.QSqlTableModel()
        # self.model1.setTable('work_cost')  # название таблицы, а не БД

        self.model.select()  # вывод данных из таблицы в tableView
        # инициализация БД(создание)
        self.model.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, "Децимальный №")
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, "Наименование")
        # self.model.setHeaderData(3, QtCore.Qt.Horizontal, "Материал")
        # self.model.setHeaderData(4, QtCore.Qt.Horizontal, "Норма расхода материала, кг")
        self.model.setHeaderData(3, QtCore.Qt.Horizontal, "Площадь поверхности, мм2")
        self.model.setHeaderData(4, QtCore.Qt.Horizontal, "Глубина обработки, мм")  # заменить на стоимость изделия(сложить трудоемкость и материал)
        self.model.setHeaderData(5, QtCore.Qt.Horizontal, "Трудоемкость, н/ч")
        self.model.setHeaderData(6, QtCore.Qt.Horizontal, "Себестоимость, руб. с НДС")
        # self.model1.select()
        # self.model1.setHeaderData(4, QtCore.Qt.Horizontal, "Время изготовления партии, часов")  # перевести в дни

        self.ui.tableView.setModel(self.model)
        # self.ui.tableView.setModel(self.model1)
        self.ui.tableView.setColumnHidden(0, True)  # скрытие столбцов
        self.ui.tableView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.ui.tableView.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        """Вставить данные из таблиц work_cost и material_cost"""

    def onPBRaschetclicked(self):
        self.mykalkul.setParameters(self.ui.LENaimenovanie.text(),
                                    self.ui.LEArticul.text(),
                                    self.ui.LEKolichestvo.text(),
                                    self.ui.LEPloshad.text(),
                                    self.ui.LEGlubina.text())
        self.mykalkul.start()
        print('onPBRaschetclicked')
        """Привязать к таблице с ценами на материал добавить параметры, """

    def onPBSaveclicked(self):
        index = self.model.rowCount()
        self.model.insertRows(index, 1)
        self.model.setData(self.model.index(index, 1), self.ui.LEArticul.text())
        self.model.setData(self.model.index(index, 2), self.ui.LENaimenovanie.text())
        self.model.setData(self.model.index(index, 3), self.ui.LEPloshad.text())  # LEMaterial
        self.model.setData(self.model.index(index, 4), self.ui.LEGlubina.text())  # LEMaterialrate
        self.model.setData(self.model.index(index, 5), self.ui.LETrudoemkost.text())
        self.model.setData(self.model.index(index, 6), self.ui.LESebestoimost.text())
        #self.model1.setData(self.model1.index(index, 4), self.ui.LEVremyapartii.text())   # заменить на столбец из таблицы work_cost
        self.model.submitAll()
        print('onPBSaveclicked')
        """Добавить сохранение в данных в таблицу work_cost"""

    def onPBMoveclicked(self):
        if self.ui.tableView.currentIndex().row() > -1:
            index_list = []
            for model_index in self.ui.tableView.selectionModel().selectedRows():
                index = QtCore.QPersistentModelIndex(model_index)
                index_list.append(index)
            for index in index_list:
                 self.model.removeRow(index.row())
            self.model.select()  # update tableView
        else:
            QtWidgets.QMessageBox.about(self, 'Message', 'Выберите строку')
        print("onPBMoveClicked")


    def onPBExtractclicked(self):
        new_reestr = Extractor()
        new_reestr.init_tables()
        new_reestr.close()  # разобраться с выгрузкой файла, сразу при нажатии кнопки.
        new_reestr.show()
        print("onPBExtractclicked")
        """При внесении изменений пользователем в файле - какой сохранится вариант файла"""

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
        if event.type() == QtCore.QEvent.Type.Close:
            event.setAccepted(False)
        return QtWidgets.QMainWindow.event(self, event)


if __name__ == '__main__':

    app = QtWidgets.QApplication()
    widget = KalkulationWindow()
    widget.show()
    app.exec_()
