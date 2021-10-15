import sys
from PySide2 import QtWidgets, QtCore, QtGui, QtSql
import kalkulation_window
import kalkulation_core
import sqlite3
#import temp
from xlsx_extractor import Extractor


class KalkulationWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        print('init')
        QtWidgets.QMainWindow.__init__(self, parent)
        self.mykalkul_core = kalkulation_core.MyKalkulationCore()  # экземпляр класса MyKalkulationCore
        self.ui = kalkulation_window.Ui_MainWindow()  # # экземпляр класса Ui_MainWindow
        self.ui.setupUi(self)
        #self.ui.LETrudoemkost.setHidden(True)
        #self.ui.LESebestoimost.setHidden(True)
        #self.ui.LEVremyapartii.setHidden(True)

        validator = QtCore.QRegExp("[0-9]+[.]?[0-9]{,2}")
        ok = QtGui.QRegExpValidator(validator, self)
        self.ui.LEarea.setValidator(ok)
        self.ui.LEarea.setFocus()
        self.ui.LEMaterialrate.setValidator(ok)
        self.ui.LEMaterialrate.setFocus()
        self.ui.LEdeep.setValidator(ok)
        self.ui.LEdeep.setFocus()
        self.ui.LEarea.setValidator(ok)
        self.ui.LEarea.setFocus()
        self.ui.LEamount.setValidator(ok)
        self.ui.LEamount.setFocus()


        self.initSqlModel()
        self.ui.PBSaved.clicked.connect(self.onPBSaveclicked)
        self.ui.PBRaschet.clicked.connect(self.onPBRaschetclicked)
        self.ui.PBMoved.clicked.connect(self.onPBMoveclicked)
        self.ui.PBExtract.clicked.connect(self.onPBExtractclicked)
        self.mykalkul_core.signalTrudoemkost.connect(self.setLineEditTrudoemkost, QtCore.Qt.QueuedConnection)
        self.mykalkul_core.signalSebestoimost.connect(self.setLineEditSebestoimost, QtCore.Qt.QueuedConnection)
        self.mykalkul_core.signalVremyapartii.connect(self.setLineEditVremyaPartii, QtCore.Qt.QueuedConnection)

    def setLineEditTrudoemkost(self, text):
        self.ui.LETrudoemkost.setText(text)

    def setLineEditSebestoimost(self, text):
        self.ui.LESebestoimost.setText(text)

    def setLineEditVremyaPartii(self, text):
        self.ui.LEVremyapartii.setText(text)

    # def setLineEditMaterial(self, text):
    #     self.ui.LEMaterial.setText(text)

    def initSqlModel(self):
        self.db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('fieldlist_var2.db')
        self.model = QtSql.QSqlTableModel()

        """Где то здесь прописать в переменную JOIN двух таблиц и ввести переменную как аргумент setTable?"""
        self.model.setTable('fieldlist')  # название таблицы fieldlist, а не БД
        # self.model1 = QtSql.QSqlTableModel()
        # self.model1.setTable('work_cost')  # название таблицы, а не БД

        self.model.select()  # вывод данных из таблицы в tableView
        # инициализация столбцов в tableVeiw
        self.model.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, "Децимальный №")
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, "Наименование")
        # self.model.setHeaderData(3, QtCore.Qt.Horizontal, "Материал")
        # self.model.setHeaderData(4, QtCore.Qt.Horizontal, "Норма расхода материала, кг")
        self.model.setHeaderData(3, QtCore.Qt.Horizontal, "Площадь поверхности, мм2")
        self.model.setHeaderData(4, QtCore.Qt.Horizontal, "Глубина обработки, мм")
        self.model.setHeaderData(5, QtCore.Qt.Horizontal, "Трудоемкость, н/ч")
        self.model.setHeaderData(6, QtCore.Qt.Horizontal, "Себестоимость, руб. с НДС")
        # self.model1.select()
        # self.model1.setHeaderData(4, QtCore.Qt.Horizontal, "Время изготовления партии, дней")

        self.ui.tableView.setModel(self.model)
        self.ui.tableView.setColumnHidden(0, True)  # скрытие столбцов
        self.ui.tableView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.ui.tableView.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        """Вставить данные из таблиц work_cost и material_cost"""

    def onPBRaschetclicked(self):
        self.mykalkul_core.setParameters(self.ui.LENaimenovanie.text(),
                                         self.ui.LEArticul.text(),
                                         self.ui.LEamount.text(),
                                         self.ui.LEarea.text(),
                                         self.ui.LEdeep.text(),
                                         self.ui.LEMaterial.text(),
                                         self.ui.LEMaterialrate.text())
        self.mykalkul_core.start()
        print('onPBRaschetclicked')
        """Привязать к таблице с ценами на материал добавить параметры"""

    def onPBSaveclicked(self):
        index = self.model.rowCount()
        self.model.insertRows(index, 1)
        self.model.setData(self.model.index(index, 1), self.ui.LEArticul.text())
        self.model.setData(self.model.index(index, 2), self.ui.LENaimenovanie.text())
        self.model.setData(self.model.index(index, 3), self.ui.LEarea.text())  # LEMaterial
        self.model.setData(self.model.index(index, 4), self.ui.LEdeep.text())  # LEMaterialrate
        self.model.setData(self.model.index(index, 5), self.ui.LETrudoemkost.text())
        self.model.setData(self.model.index(index, 6), self.ui.LESebestoimost.text())
        #self.model1.setData(self.model1.index(index, 4), self.ui.LEVremyapartii.text())   # заменить на столбец из таблицы work_cost
        self.model.submitAll()
        print('onPBSaveclicked')
        #print(self.ui.LENaimenovanie.text())
        fieldlist_ = []
        connect_to_db = sqlite3.connect('fieldlist_var2.db')
        with connect_to_db:
            cursor_fieldlist_ = connect_to_db.cursor()
            cursor_fieldlist_.execute(f"INSERT INTO work_cost(detail, labour, work_cost_rub, time_days)"
                                      f"VALUES ('{self.ui.LENaimenovanie.text()}', {self.ui.LETrudoemkost.text()}, {self.ui.LESebestoimost.text()}, {self.ui.LETrudoemkost.text()}/(3600*7.5))")
            for row in cursor_fieldlist_:
                fieldlist_.append(row)
            print(fieldlist_)

            """Traceback (most recent call last):
                File "C:\python\VKR\pyqtexam\main.py", line 105, in onPBSaveclicked
                cursor_fieldlist_.execute(f"INSERT INTO work_cost(detail, labour, work_cost_rub, time_days)"
                sqlite3.OperationalError: database is locked"""

        """Добавить сохранение в данных в таблицу work_cost(insert)"""

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
