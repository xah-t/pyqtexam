# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Kalkulation.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 850)
        MainWindow.setMinimumSize(QSize(0, 0))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        """
        self.table = QTableWidget(self.centralwidget)  # Создаём таблицу
        self.table.setGeometry(QRect(10, 337, 1180, 400))
        self.table.setColumnCount(4)  # Устанавливаем три колонки
        self.table.setRowCount(1)  # и одну строку в таблице

        # Устанавливаем заголовки таблицы
        self.table.setHorizontalHeaderLabels(["Децимальный Номер", "Наименование", "Трудоёмкость", "Себестоимость"])

        # Устанавливаем выравнивание на заголовки
        self.table.horizontalHeaderItem(0).setTextAlignment(Qt.AlignLeft)
        self.table.horizontalHeaderItem(1).setTextAlignment(Qt.AlignHCenter)
        self.table.horizontalHeaderItem(2).setTextAlignment(Qt.AlignRight)
        self.table.horizontalHeaderItem(3).setTextAlignment(Qt.AlignRight)
        """
        self.tableView_1 = QTableView(self.centralwidget)
        self.tableView_1.setObjectName(u"tableView_1")
        self.tableView_1.setGeometry(QRect(10, 337, 1180, 400))  # Изначальная ширина 860
        self.tableView_1.setMinimumSize(QSize(1180, 400))
        self.tableView_1.setMaximumSize(QSize(16777215, 16777215))
        """
        """#Выключил две tableView, т.к. не синхронизируется скролл"""
        # self.tableView_2 = QTableView(self.centralwidget)
        # self.tableView_2.setObjectName(u"tableView_2")
        # self.tableView_2.setGeometry(QRect(669, 337, 161, 400))
        # self.tableView_2.setMinimumSize(QSize(260, 400))
        # self.tableView_2.setMaximumSize(QSize(16777215, 16777215))
        # self.tableView_3 = QTableView(self.centralwidget)
        # self.tableView_3.setObjectName(u"tableView_3")
        # self.tableView_3.setGeometry(QRect(929, 337, 160, 400))
        # self.tableView_3.setMinimumSize(QSize(260, 400))
        # self.tableView_3.setMaximumSize(QSize(16777215, 16777215))
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 739, 1181, 41))
        self.gridLayout_2 = QGridLayout(self.layoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.PBMoved = QPushButton(self.layoutWidget)
        self.PBMoved.setObjectName(u"PBMoved")
        self.PBMoved.setMaximumSize(QSize(16777215, 45))

        self.gridLayout_2.addWidget(self.PBMoved, 0, 0, 1, 1)

        self.PBSaved = QPushButton(self.layoutWidget)
        self.PBSaved.setObjectName(u"PBSaved")
        self.PBSaved.setMaximumSize(QSize(16777215, 45))

        self.gridLayout_2.addWidget(self.PBSaved, 0, 1, 1, 1)

        self.PBExtract = QPushButton(self.layoutWidget)
        self.PBExtract.setObjectName(u"PBExtract")
        self.PBExtract.setMaximumSize(QSize(16777215, 45))

        self.gridLayout_2.addWidget(self.PBExtract, 0, 2, 1, 1)

        self.textEdit_11 = QTextEdit(self.centralwidget)
        self.textEdit_11.setObjectName(u"textEdit_11")
        self.textEdit_11.setEnabled(False)
        self.textEdit_11.setGeometry(QRect(10, 310, 388, 27))
        self.textEdit_11.setMaximumSize(QSize(16777215, 30))
        self.textEdit_11.setReadOnly(True)
        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 12, 1181, 291))
        self.gridLayout = QGridLayout(self.layoutWidget1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.textEdit_4 = QTextEdit(self.layoutWidget1)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setEnabled(False)
        self.textEdit_4.setMaximumSize(QSize(16777215, 30))
        self.textEdit_4.setReadOnly(True)

        self.gridLayout.addWidget(self.textEdit_4, 0, 0, 1, 1)

        self.textEdit_5 = QTextEdit(self.layoutWidget1)
        self.textEdit_5.setObjectName(u"textEdit_5")
        self.textEdit_5.setEnabled(False)
        self.textEdit_5.setMaximumSize(QSize(16777215, 30))
        self.textEdit_5.setReadOnly(True)

        self.gridLayout.addWidget(self.textEdit_5, 0, 1, 1, 1)

        self.textEdit_6 = QTextEdit(self.layoutWidget1)
        self.textEdit_6.setObjectName(u"textEdit_6")
        self.textEdit_6.setEnabled(False)
        self.textEdit_6.setMaximumSize(QSize(16777215, 30))
        self.textEdit_6.setReadOnly(True)

        self.gridLayout.addWidget(self.textEdit_6, 0, 2, 1, 1)

        self.LEname = QLineEdit(self.layoutWidget1)
        self.LEname.setObjectName(u"LEname")
        self.LEname.setMaximumSize(QSize(16777215, 30))

        self.gridLayout.addWidget(self.LEname, 1, 0, 1, 1)

        self.LEArticul = QLineEdit(self.layoutWidget1)
        self.LEArticul.setObjectName(u"LEArticul")
        self.LEArticul.setMaximumSize(QSize(16777215, 30))

        self.gridLayout.addWidget(self.LEArticul, 1, 1, 1, 1)

        self.LEamount = QLineEdit(self.layoutWidget1)
        self.LEamount.setObjectName(u"LEamount")
        self.LEamount.setMaximumSize(QSize(16777215, 30))

        self.gridLayout.addWidget(self.LEamount, 1, 2, 1, 1)

        self.textEdit_8 = QTextEdit(self.layoutWidget1)
        self.textEdit_8.setObjectName(u"textEdit_8")
        self.textEdit_8.setEnabled(False)
        self.textEdit_8.setMaximumSize(QSize(16777215, 30))
        self.textEdit_8.setReadOnly(True)

        self.gridLayout.addWidget(self.textEdit_8, 2, 0, 1, 1)

        self.textEdit_10 = QTextEdit(self.layoutWidget1)
        self.textEdit_10.setObjectName(u"textEdit_10")
        self.textEdit_10.setEnabled(False)
        self.textEdit_10.setMaximumSize(QSize(16777215, 30))
        self.textEdit_10.setReadOnly(True)

        self.gridLayout.addWidget(self.textEdit_10, 2, 1, 1, 1)

        self.PBRaschet = QPushButton(self.layoutWidget1)
        self.PBRaschet.setObjectName(u"PBRaschet")
        self.PBRaschet.setMinimumSize(QSize(200, 30))
        self.PBRaschet.setMaximumSize(QSize(16777215, 45))

        self.gridLayout.addWidget(self.PBRaschet, 2, 2, 2, 1)

        self.LEMaterial = QLineEdit(self.layoutWidget1)
        self.LEMaterial.setObjectName(u"LEMaterial")
        self.LEMaterial.setMaximumSize(QSize(16777215, 30))

        self.gridLayout.addWidget(self.LEMaterial, 3, 0, 1, 1)

        self.LEMaterialrate = QLineEdit(self.layoutWidget1)
        self.LEMaterialrate.setObjectName(u"LEMaterialrate")
        self.LEMaterialrate.setMaximumSize(QSize(16777215, 30))

        self.gridLayout.addWidget(self.LEMaterialrate, 3, 1, 1, 1)

        self.textEdit_9 = QTextEdit(self.layoutWidget1)
        self.textEdit_9.setObjectName(u"textEdit_9")
        self.textEdit_9.setEnabled(False)
        self.textEdit_9.setMaximumSize(QSize(16777215, 30))
        self.textEdit_9.setReadOnly(True)

        self.gridLayout.addWidget(self.textEdit_9, 4, 0, 1, 1)

        self.textEdit_7 = QTextEdit(self.layoutWidget1)
        self.textEdit_7.setObjectName(u"textEdit_7")
        self.textEdit_7.setEnabled(False)
        self.textEdit_7.setMaximumSize(QSize(16777215, 30))
        self.textEdit_7.setReadOnly(True)

        self.gridLayout.addWidget(self.textEdit_7, 4, 1, 1, 1)

        self.LEdeep = QLineEdit(self.layoutWidget1)
        self.LEdeep.setObjectName(u"LEdeep")
        self.LEdeep.setMinimumSize(QSize(200, 0))
        self.LEdeep.setMaximumSize(QSize(16777215, 30))

        self.gridLayout.addWidget(self.LEdeep, 5, 0, 1, 1)

        self.LEarea = QLineEdit(self.layoutWidget1)
        self.LEarea.setObjectName(u"LEarea")
        self.LEarea.setMinimumSize(QSize(200, 0))
        self.LEarea.setMaximumSize(QSize(16777215, 30))

        self.gridLayout.addWidget(self.LEarea, 5, 1, 1, 1)

        self.textEdit_2 = QTextEdit(self.layoutWidget1)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setEnabled(False)
        self.textEdit_2.setMaximumSize(QSize(16777215, 30))
        self.textEdit_2.setReadOnly(True)

        self.gridLayout.addWidget(self.textEdit_2, 6, 0, 1, 1)

        self.textEdit = QTextEdit(self.layoutWidget1)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setEnabled(False)
        self.textEdit.setMaximumSize(QSize(16777215, 30))
        self.textEdit.setReadOnly(True)

        self.gridLayout.addWidget(self.textEdit, 6, 1, 1, 1)

        self.textEdit_3 = QTextEdit(self.layoutWidget1)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setEnabled(False)
        self.textEdit_3.setMaximumSize(QSize(16777215, 30))
        self.textEdit_3.setReadOnly(True)

        self.gridLayout.addWidget(self.textEdit_3, 6, 2, 1, 1)

        self.LEprimecost = QLineEdit(self.layoutWidget1)
        self.LEprimecost.setObjectName(u"LEprimecost")
        self.LEprimecost.setMaximumSize(QSize(16777215, 30))

        self.gridLayout.addWidget(self.LEprimecost, 7, 0, 1, 1)

        self.LElabour = QLineEdit(self.layoutWidget1)
        self.LElabour.setObjectName(u"LElabour")
        self.LElabour.setMaximumSize(QSize(16777215, 30))

        self.gridLayout.addWidget(self.LElabour, 7, 1, 1, 1)

        self.LEproductiontime = QLineEdit(self.layoutWidget1)
        self.LEproductiontime.setObjectName(u"LEproductiontime")
        self.LEproductiontime.setMaximumSize(QSize(16777215, 30))

        self.gridLayout.addWidget(self.LEproductiontime, 7, 2, 1, 1)


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1200, 26))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addSeparator()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Kalkulation", None))
        self.PBMoved.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0440\u0430\u0441\u0447\u0435\u0442 \u0438\u0437 \u0420\u0435\u0435\u0441\u0442\u0440\u0430", None))
        self.PBSaved.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0440\u0430\u0441\u0447\u0435\u0442 \u0432 \u0420\u0435\u0435\u0441\u0442\u0440", None))
        self.PBExtract.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0432\u0435\u0441\u0442\u0438 \u0420\u0435\u0435\u0441\u0442\u0440 \u0432 Excel", None))
        self.textEdit_11.setMarkdown(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0447\u0435\u043d\u044c \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u043d\u044b\u0445 \u0440\u0430\u0441\u0447\u0435\u0442\u043e\u0432\n"
"\n"
"", None))
        self.textEdit_11.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:5px; margin-bottom:5px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt;\">\u041f\u0435\u0440\u0435\u0447\u0435\u043d\u044c \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u043d\u044b\u0445 \u0440\u0430\u0441\u0447\u0435\u0442\u043e\u0432</span></p></body></html>", None))
        self.textEdit_4.setMarkdown(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435\n"
"\n"
"", None))
        self.textEdit_4.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:5px; margin-bottom:5px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt;\">\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435</span></p></body></html>", None))
        self.textEdit_5.setMarkdown(QCoreApplication.translate("MainWindow", u"\u0410\u0440\u0442\u0438\u043a\u0443\u043b\n"
"\n"
"", None))
        self.textEdit_5.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:5px; margin-bottom:5px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt;\">\u0410\u0440\u0442\u0438\u043a\u0443\u043b</span></p></body></html>", None))
        self.textEdit_6.setMarkdown(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u043c\u0435\u0440 \u043f\u0430\u0440\u0442\u0438\u0438, \u0448\u0442.\n"
"\n"
"", None))
        self.textEdit_6.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:5px; margin-bottom:5px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt;\">\u0420\u0430\u0437\u043c\u0435\u0440 \u043f\u0430\u0440\u0442\u0438\u0438, \u0448\u0442.</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.LEname.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.LEname.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.LEname.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.LEname.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.LEname.setInputMask("")
        self.LEname.setText("")
        self.LEname.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u0434\u0435\u0442\u0430\u043b\u0438", None))
        self.LEArticul.setInputMask("")
        self.LEArticul.setText("")
        self.LEArticul.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0430\u0440\u0442\u0438\u043a\u0443\u043b \u0434\u0435\u0442\u0430\u043b\u0438", None))
        self.LEamount.setInputMask("")
        self.LEamount.setText("")
        self.LEamount.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0434\u0435\u0442\u0430\u043b\u0435\u0439, \u0448\u0442.", None))
        self.textEdit_8.setMarkdown(QCoreApplication.translate("MainWindow", u"\u041c\u0430\u0440\u043a\u0430 \u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b\u0430\n"
"\n"
"", None))
        self.textEdit_8.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:5px; margin-bottom:5px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt;\">\u041c\u0430\u0440\u043a\u0430 \u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b\u0430</span></p></body></html>", None))
        self.textEdit_10.setMarkdown(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0440\u043c\u0430 \u0440\u0430\u0441\u0445\u043e\u0434\u0430 \u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b\u0430, \u043a\u0433\n"
"\n"
"", None))
        self.textEdit_10.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:5px; margin-bottom:5px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt;\">\u041d\u043e\u0440\u043c\u0430 \u0440\u0430\u0441\u0445\u043e\u0434\u0430 \u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b\u0430, \u043a\u0433</span></p></body></html>", None))
        self.PBRaschet.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0447\u0438\u0442\u0430\u0442\u044c", None))
#if QT_CONFIG(tooltip)
        self.LEMaterial.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.LEMaterial.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.LEMaterial.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.LEMaterial.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.LEMaterial.setInputMask("")
        self.LEMaterial.setText("")
        self.LEMaterial.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043c\u0430\u0440\u043a\u0443 \u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b\u0430", None))
#if QT_CONFIG(tooltip)
        self.LEMaterialrate.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.LEMaterialrate.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.LEMaterialrate.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.LEMaterialrate.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.LEMaterialrate.setInputMask("")
        self.LEMaterialrate.setText("")
        self.LEMaterialrate.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043d.\u0440. \u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b\u0430 \u043d\u0430 \u0434\u0435\u0442\u0430\u043b\u044c, \u043a\u0433", None))
        self.textEdit_9.setMarkdown(QCoreApplication.translate("MainWindow", u"\u0413\u043b\u0443\u0431\u0438\u043d\u0430 \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0438, \u043c\u043c\n"
"\n"
"", None))
        self.textEdit_9.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:5px; margin-bottom:5px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0413\u043b\u0443\u0431\u0438\u043d\u0430 \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0438, \u043c\u043c</p></body></html>", None))
        self.textEdit_7.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u041f\u043b\u043e\u0449\u0430\u0434\u044c \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0438, \u043c\u043c2</p></body></html>", None))
        self.LEdeep.setText("")
        self.LEdeep.setPlaceholderText(QCoreApplication.translate("MainWindow", u"mm", None))
        self.LEarea.setInputMask("")
        self.LEarea.setText("")
        self.LEarea.setPlaceholderText(QCoreApplication.translate("MainWindow", u"mm2", None))
        self.textEdit_2.setMarkdown(QCoreApplication.translate("MainWindow", u"\u0421\u0435\u0431\u0435\u0441\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c, \u0440\u0443\u0431. \u0441 \u041d\u0414\u0421\n"
"\n"
"", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:5px; margin-bottom:5px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt;\">\u0421\u0435\u0431\u0435\u0441\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c, \u0440\u0443\u0431. \u0441 \u041d\u0414\u0421</span></p></body></html>", None))
        self.textEdit.setMarkdown(QCoreApplication.translate("MainWindow", u"\u0422\u0440\u0443\u0434\u043e\u0451\u043c\u043a\u043e\u0441\u0442\u044c  \u043d/\u0447\n"
"\n"
"", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:5px; margin-bottom:5px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt;\">\u0422\u0440\u0443\u0434\u043e\u0451\u043c\u043a\u043e\u0441\u0442\u044c  \u043d/\u0447</span></p></body></html>", None))
        self.textEdit_3.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0421\u0440\u043e\u043a \u0438\u0437\u0433\u043e\u0442\u043e\u0432\u043b\u043d\u0435\u043d\u0438\u044f \u043f\u0430\u0440\u0442\u0438\u0438, \u0434\u043d\u0435\u0439</p></body></html>", None))
        self.LEprimecost.setInputMask("")
        self.LEprimecost.setText("")
        self.LEprimecost.setPlaceholderText("")
        self.LElabour.setInputMask("")
        self.LElabour.setText("")
        self.LElabour.setPlaceholderText("")
        self.LEproductiontime.setText("")
        self.LEproductiontime.setPlaceholderText("")
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u0440\u0430\u0441\u0447\u0435\u0442", None))
    # retranslateUi

