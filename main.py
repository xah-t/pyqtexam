import sys
import kalkulation_window2
#import kalkulation_window_scrollarea
import kalkulation_core
import sqlite3
from PySide2 import QtWidgets, QtCore, QtGui, QtSql
from xlsx_extractor import Extractor
"""PySide2-uic kalkulation_window_scrollarea.ui -o kalkulation_window_scrollarea.py"""

class KalkulationWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        print('init')
        QtWidgets.QMainWindow.__init__(self, parent)
        self.mykalkul_core = kalkulation_core.MyKalkulationCore()  # экземпляр класса MyKalkulationCore
        self.ui = kalkulation_window2.Ui_MainWindow()
        #self.ui = kalkulation_window_scrollarea.Ui_MainWindow()# # экземпляр класса Ui_MainWindow kalkulation_window_scrollarea
        self.ui.setupUi(self)
        #self.ui.LElabour.setHidden(True)
        #self.ui.LEprimecost.setHidden(True)
        #self.ui.LEproductiontime.setHidden(True)

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
        self.mykalkul_core.signallabour.connect(self.setLineEditlabour, QtCore.Qt.QueuedConnection)
        self.mykalkul_core.signalprimecost.connect(self.setLineEditprimecost, QtCore.Qt.QueuedConnection)
        self.mykalkul_core.signalproductiontime.connect(self.setLineEditproductiontime, QtCore.Qt.QueuedConnection)

    def setLineEditlabour(self, text):
        self.ui.LElabour.setText(text)

    def setLineEditprimecost(self, text):
        self.ui.LEprimecost.setText(text)

    def setLineEditproductiontime(self, text):
        self.ui.LEproductiontime.setText(text)

    def initSqlModel(self):
        self.db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('fieldlist_var2.db')
        self.model = QtSql.QSqlTableModel()
        self.model1 = QtSql.QSqlTableModel()

        """Где то здесь прописать в переменную JOIN двух таблиц и ввести переменную как аргумент setTable?"""
        #connection_for_table_view = sqlite3.connect('fieldlist_var2.db')
        #cursor_connection_for_table_view = connection_for_table_view.cursor()
        #cursor_connection_for_table_view.execute('SELECT fieldlist.articul, fieldlist.name, work_cost.work_cost_rub, work_cost.time_days, material_cost.material_cost_rub FROM fieldlist'
        #                                         ' LEFT JOIN work_cost ON fieldlist.articul = work_cost.detail'
        #                                        ' LEFT JOIN material_cost ON fieldlist.material = material_cost.material_mark')

        """JOIN"""
        """JOIN"""
        """JOIN"""
        """JOIN"""

        self.model.setTable('fieldlist')  # название таблицы fieldlist, а не БД
        self.model.select()  # вывод данных из таблицы в tableView_1
        self.model1.setTable('work_cost')
        self.model1.select()
        # инициализация столбцов в tableView_1
        self.model.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, "Децимальный №")
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, "Наименование")
        # self.model.setHeaderData(3, QtCore.Qt.Horizontal, "Материал")
        # self.model.setHeaderData(4, QtCore.Qt.Horizontal, "Норма расхода материала, кг")
        self.model.setHeaderData(5, QtCore.Qt.Horizontal, "Площадь обработки, мм2")
        self.model.setHeaderData(6, QtCore.Qt.Horizontal, "Глубина обработки, мм")
        self.model1.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
        self.model1.setHeaderData(1, QtCore.Qt.Horizontal, "Idetail")
        self.model1.setHeaderData(0, QtCore.Qt.Horizontal, "labour")

        self.ui.tableView_1.setModel(self.model)
        self.ui.tableView_1.setColumnHidden(0, True)  # скрытие столбцов
        self.ui.tableView_1.setColumnHidden(3, True)
        self.ui.tableView_1.setColumnHidden(4, True)
        self.ui.tableView_1.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.ui.tableView_1.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        # self.ui.tableView_2.setModel(self.model1)
        # self.ui.tableView_2.setColumnHidden(0, True)  # скрытие столбцов
        # self.ui.tableView_2.setColumnHidden(1, True)
        # self.ui.tableView_2.setColumnHidden(3, True)
        """Вставить данные из таблиц work_cost и material_cost"""

    def onPBRaschetclicked(self):
        self.mykalkul_core.setParameters(self.ui.LEname.text(),
                                         self.ui.LEArticul.text(),
                                         self.ui.LEamount.text(),
                                         self.ui.LEarea.text(),
                                         self.ui.LEdeep.text(),
                                         self.ui.LEMaterial.text(),
                                         self.ui.LEMaterialrate.text())
        self.mykalkul_core.start()
        print('onPBRaschetclicked')

    def onPBSaveclicked(self):
        index = self.model.rowCount()
        self.model.insertRows(index, 1)
        self.model.setData(self.model.index(index, 1), self.ui.LEArticul.text())
        self.model.setData(self.model.index(index, 2), self.ui.LEname.text())
        self.model.setData(self.model.index(index, 3), self.ui.LEMaterial.text())
        self.model.setData(self.model.index(index, 4), self.ui.LEMaterialrate.text())
        self.model.setData(self.model.index(index, 5), self.ui.LEarea.text())
        self.model.setData(self.model.index(index, 6), self.ui.LEdeep.text())
        self.model.submitAll()
        print('onPBSaveclicked')
        fieldlist_ = []
        connect_to_db = sqlite3.connect('fieldlist_var2.db')
        with connect_to_db:
            cursor_fieldlist_ = connect_to_db.cursor()
            cursor_fieldlist_.execute(f"INSERT INTO work_cost(detail, labour, work_cost_rub, time_days)"
                                      f"VALUES ('{self.ui.LEArticul.text()}', {self.ui.LElabour.text()}, {self.ui.LElabour.text()} * 2350, {self.ui.LEproductiontime.text()})")
            for row in cursor_fieldlist_:
                fieldlist_.append(row)

    def onPBMoveclicked(self):
        if self.ui.tableView_1.currentIndex().row() > -1:
            index_list = []
            for model_index in self.ui.tableView_1.selectionModel().selectedRows():
                index = QtCore.QPersistentModelIndex(model_index)
                index_list.append(index)
            for index in index_list:
                 self.model.removeRow(index.row())
            self.model.select()  # update tableView_1
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
