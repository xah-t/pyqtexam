import sys
import kalkulation_window
import kalkulation_core
import sqlite3
from PySide2 import QtWidgets, QtCore, QtGui, QtSql
from xlsx_extractor import Extractor


class KalkulationWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.mykalkul_core = kalkulation_core.MyKalkulationCore()
        self.ui = kalkulation_window.Ui_MainWindow()
        self.ui.setupUi(self)

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

        self.updateModelForView()
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

    def updateModelForView(self):
        self.db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('fieldlist_var2.db')
        self.db.open()
        self.model_for_view = QtSql.QSqlQueryModel()
        self.query_ = str(
            "SELECT fieldlist.articul, fieldlist.name, work_cost.labour, work_cost.work_cost_rub + "
            "material_cost.material_cost_rub * fieldlist.material_rate_kg FROM fieldlist "
            "LEFT JOIN work_cost ON fieldlist.articul = work_cost.detail "
            "LEFT JOIN material_cost ON fieldlist.material = material_cost.material_mark"
            )
        self.model_for_view.setQuery(self.query_)
        self.model_for_view.setHeaderData(0, QtCore.Qt.Horizontal, "Артикул детали")
        self.model_for_view.setHeaderData(1, QtCore.Qt.Horizontal, "Наименование детали")
        self.model_for_view.setHeaderData(2, QtCore.Qt.Horizontal, "Трудоёмкость, н/ч")
        self.model_for_view.setHeaderData(3, QtCore.Qt.Horizontal, "Себестоимость, руб. с НДС")
        self.ui.tableView_1.setModel(self.model_for_view)
        self.ui.tableView_1.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.ui.tableView_1.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)

    def initSqlModel(self):
        self.db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('fieldlist_var2.db')
        self.db.open()
        self.model = QtSql.QSqlTableModel()
        self.model.setTable('fieldlist')
        self.model.select()

    def onPBRaschetclicked(self):
        self.mykalkul_core.setParameters(self.ui.LEname.text(),
                                         self.ui.LEArticul.text(),
                                         self.ui.LEamount.text(),
                                         self.ui.LEarea.text(),
                                         self.ui.LEdeep.text(),
                                         self.ui.LEMaterial.text(),
                                         self.ui.LEMaterialrate.text())
        self.mykalkul_core.start()

    def onPBSaveclicked(self):
        index = self.model.rowCount()
        self.model.insertRows(index, 1)
        self.model.setData(self.model.index(index, 1), self.ui.LEArticul.text())
        self.model.setData(self.model.index(index, 2), self.ui.LEname.text())
        self.model.setData(self.model.index(index, 3), self.ui.LEMaterial.text())
        self.model.setData(self.model.index(index, 4), self.ui.LEMaterialrate.text())
        self.model.setData(self.model.index(index, 5), self.ui.LEarea.text())
        self.model.setData(self.model.index(index, 6), self.ui.LEdeep.text())

        value_ = self.ui.LEArticul.text()
        if Extractor.check_input_in_db(value_):
            QtWidgets.QMessageBox.about(self, 'Message', f"Деталь {self.ui.LEArticul.text()} уже заведена в базу.")
            self.model.revertAll()
        else:
            self.model.submitAll()
            connect_to_db = sqlite3.connect('fieldlist_var2.db')
            with connect_to_db:  # разобраться, что за оператор такой фитрый
                cursor_work_cost_ = connect_to_db.cursor()
                cursor_work_cost_.execute(f"INSERT INTO work_cost(detail, labour, work_cost_rub, time_days)"
                                          f"VALUES ('{self.ui.LEArticul.text()}', {self.ui.LElabour.text()}, {self.ui.LElabour.text()} * 2350, {self.ui.LEproductiontime.text()})"
                                          )
        self.updateModelForView()

    def onPBMoveclicked(self):
        if self.ui.tableView_1.currentIndex().row() > -1:
            index_list = []
            for model_index in self.ui.tableView_1.selectionModel().selectedRows():
                index = QtCore.QPersistentModelIndex(model_index)
                index_list.append(index)
            for index in index_list:
                self.model.removeRow(index.row())
            self.model.select()
            self.updateModelForView()
        else:
            QtWidgets.QMessageBox.about(self, 'Message', 'Выберите строку для удаления!')

    def onPBExtractclicked(self):
        new_reestr = Extractor()
        new_reestr.init_tables()
        new_reestr.close()
        new_reestr.show()

    def closeEvent(self, event: QtCore.QEvent.Close):
        reply = QtWidgets.QMessageBox.question(self, "Выход", "Вы действительно хотите выйти?")
        print(reply)
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        elif reply == QtWidgets.QMessageBox.No:
            event.ignore()

    def event(self, event: QtCore.QEvent) -> bool:
        if event.type() == QtCore.QEvent.Type.Close:
            event.setAccepted(False)
        return QtWidgets.QMainWindow.event(self, event)


if __name__ == '__main__':

    app = QtWidgets.QApplication()
    widget = KalkulationWindow()
    widget.show()
    app.exec_()
