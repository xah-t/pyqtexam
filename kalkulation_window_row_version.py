from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(881, 815)
        MainWindow.setMinimumSize(QSize(0, 0))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(40, 220, 801, 51))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textEdit = QTextEdit(self.layoutWidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setEnabled(False)
        self.textEdit.setReadOnly(True)

        self.verticalLayout.addWidget(self.textEdit)

        self.LElabour = QLineEdit(self.layoutWidget)
        self.LElabour.setObjectName(u"LETrudoemkost")

        self.verticalLayout.addWidget(self.LElabour)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.textEdit_2 = QTextEdit(self.layoutWidget)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setEnabled(False)
        self.textEdit_2.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.textEdit_2)

        self.LEprimecost = QLineEdit(self.layoutWidget)
        self.LEprimecost.setObjectName(u"LESebestoimost")

        self.verticalLayout_2.addWidget(self.LEprimecost)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.textEdit_3 = QTextEdit(self.layoutWidget)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setEnabled(False)
        self.textEdit_3.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.textEdit_3)

        self.LEproductiontime = QLineEdit(self.layoutWidget)
        self.LEproductiontime.setObjectName(u"LEVremyapartii")

        self.verticalLayout_3.addWidget(self.LEproductiontime)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(40, 630, 801, 25))
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.PBSaved = QPushButton(self.widget)
        self.PBSaved.setObjectName(u"PBSaved")

        self.horizontalLayout_2.addWidget(self.PBSaved)

        self.PBMoved = QPushButton(self.widget)
        self.PBMoved.setObjectName(u"PBMoved")

        self.horizontalLayout_2.addWidget(self.PBMoved)

        self.PBExtract = QPushButton(self.widget)
        self.PBExtract.setObjectName(u"PBExtract")

        self.horizontalLayout_2.addWidget(self.PBExtract)

        self.widget1 = QWidget(self.centralwidget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(40, 279, 801, 341))
        self.verticalLayout_12 = QVBoxLayout(self.widget1)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.textEdit_11 = QTextEdit(self.widget1)
        self.textEdit_11.setObjectName(u"textEdit_11")
        self.textEdit_11.setEnabled(False)
        self.textEdit_11.setMaximumSize(QSize(16777215, 20))
        self.textEdit_11.setReadOnly(True)

        self.horizontalLayout_6.addWidget(self.textEdit_11)

        self.horizontalSpacer = QSpacerItem(528, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)


        self.verticalLayout_12.addLayout(self.horizontalLayout_6)

        self.tableView = QTableView(self.widget1)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setMinimumSize(QSize(0, 300))
        self.tableView.setMaximumSize(QSize(16777215, 500))

        self.verticalLayout_12.addWidget(self.tableView)

        self.widget2 = QWidget(self.centralwidget)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(41, 13, 798, 47))
        self.horizontalLayout = QHBoxLayout(self.widget2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.textEdit_4 = QTextEdit(self.widget2)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setEnabled(False)
        self.textEdit_4.setReadOnly(True)

        self.verticalLayout_4.addWidget(self.textEdit_4)

        self.LEname = QLineEdit(self.widget2)
        self.LEname.setObjectName(u"LENaimenovanie")

        self.verticalLayout_4.addWidget(self.LEname)


        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.textEdit_5 = QTextEdit(self.widget2)
        self.textEdit_5.setObjectName(u"textEdit_5")
        self.textEdit_5.setEnabled(False)
        self.textEdit_5.setReadOnly(True)

        self.verticalLayout_5.addWidget(self.textEdit_5)

        self.LEArticul = QLineEdit(self.widget2)
        self.LEArticul.setObjectName(u"LEArticul")

        self.verticalLayout_5.addWidget(self.LEArticul)


        self.horizontalLayout.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.textEdit_6 = QTextEdit(self.widget2)
        self.textEdit_6.setObjectName(u"textEdit_6")
        self.textEdit_6.setEnabled(False)
        self.textEdit_6.setReadOnly(True)

        self.verticalLayout_6.addWidget(self.textEdit_6)

        self.LEamount = QLineEdit(self.widget2)
        self.LEamount.setObjectName(u"LEKolichestvo")
        self.LEamount.setMaximumSize(QSize(300, 16777215))

        self.verticalLayout_6.addWidget(self.LEamount)


        self.horizontalLayout.addLayout(self.verticalLayout_6)

        self.widget3 = QWidget(self.centralwidget)
        self.widget3.setObjectName(u"widget3")
        self.widget3.setGeometry(QRect(41, 66, 798, 46))
        self.horizontalLayout_4 = QHBoxLayout(self.widget3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.textEdit_8 = QTextEdit(self.widget3)
        self.textEdit_8.setObjectName(u"textEdit_8")
        self.textEdit_8.setEnabled(False)
        self.textEdit_8.setReadOnly(True)

        self.verticalLayout_9.addWidget(self.textEdit_8)

        self.LEMaterial = QLineEdit(self.widget3)
        self.LEMaterial.setObjectName(u"LEMaterial")

        self.verticalLayout_9.addWidget(self.LEMaterial)


        self.horizontalLayout_4.addLayout(self.verticalLayout_9)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.textEdit_10 = QTextEdit(self.widget3)
        self.textEdit_10.setObjectName(u"textEdit_10")
        self.textEdit_10.setEnabled(False)
        self.textEdit_10.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.textEdit_10)

        self.LEMaterialrate = QLineEdit(self.widget3)
        self.LEMaterialrate.setObjectName(u"LEMaterialrate")

        self.verticalLayout_10.addWidget(self.LEMaterialrate)


        self.horizontalLayout_4.addLayout(self.verticalLayout_10)

        self.horizontalSpacer_2 = QSpacerItem(268, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.widget4 = QWidget(self.centralwidget)
        self.widget4.setObjectName(u"widget4")
        self.widget4.setGeometry(QRect(44, 121, 794, 51))
        self.horizontalLayout_5 = QHBoxLayout(self.widget4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.textEdit_7 = QTextEdit(self.widget4)
        self.textEdit_7.setObjectName(u"textEdit_7")
        self.textEdit_7.setEnabled(False)
        self.textEdit_7.setReadOnly(True)

        self.verticalLayout_7.addWidget(self.textEdit_7)

        self.LEarea = QLineEdit(self.widget4)
        self.LEarea.setObjectName(u"LEPloshad")
        self.LEarea.setMinimumSize(QSize(200, 0))
        self.LEarea.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_7.addWidget(self.LEarea)


        self.horizontalLayout_5.addLayout(self.verticalLayout_7)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.textEdit_9 = QTextEdit(self.widget4)
        self.textEdit_9.setObjectName(u"textEdit_9")
        self.textEdit_9.setEnabled(False)
        self.textEdit_9.setReadOnly(True)

        self.verticalLayout_8.addWidget(self.textEdit_9)

        self.LEdeep = QLineEdit(self.widget4)
        self.LEdeep.setObjectName(u"LEGlubina")
        self.LEdeep.setMinimumSize(QSize(200, 0))
        self.LEdeep.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_8.addWidget(self.LEdeep)


        self.horizontalLayout_5.addLayout(self.verticalLayout_8)

        self.horizontalSpacer_3 = QSpacerItem(58, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.PBRaschet = QPushButton(self.widget4)
        self.PBRaschet.setObjectName(u"PBRaschet")
        self.PBRaschet.setMinimumSize(QSize(200, 30))
        self.PBRaschet.setMaximumSize(QSize(300, 16777215))

        self.horizontalLayout_5.addWidget(self.PBRaschet)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 881, 21))
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
        self.textEdit.setMarkdown(QCoreApplication.translate("MainWindow", u"\u0422\u0440\u0443\u0434\u043e\u0451\u043c\u043a\u043e\u0441\u0442\u044c  \u043d/\u0447\n"
"\n"
"", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:5px; margin-bottom:5px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0422\u0440\u0443\u0434\u043e\u0451\u043c\u043a\u043e\u0441\u0442\u044c  \u043d/\u0447</p></body></html>", None))
        self.LElabour.setInputMask("")
        self.LElabour.setText("")
        self.LElabour.setPlaceholderText("")
        self.textEdit_2.setMarkdown(QCoreApplication.translate("MainWindow", u"\u0421\u0435\u0431\u0435\u0441\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c, \u0440\u0443\u0431. \u0441 \u041d\u0414\u0421\n"
"\n"
"", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:5px; margin-bottom:5px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0421\u0435\u0431\u0435\u0441\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c, \u0440\u0443\u0431. \u0441 \u041d\u0414\u0421</p></body></html>", None))
        self.LEprimecost.setInputMask("")
        self.LEprimecost.setText("")
        self.LEprimecost.setPlaceholderText("")
        self.textEdit_3.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7.8pt;\">\u0421\u0440\u043e\u043a \u0438\u0437\u0433\u043e\u0442\u043e\u0432\u043b\u043d\u0435\u043d\u0438\u044f \u043f\u0430\u0440\u0442\u0438\u0438, \u0434\u043d\u0435\u0439</span></p></body></html>", None))
        self.LEproductiontime.setText("")
        self.LEproductiontime.setPlaceholderText("")
        self.PBSaved.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0440\u0430\u0441\u0447\u0435\u0442 \u0432 \u0420\u0435\u0435\u0441\u0442\u0440", None))
        self.PBMoved.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0440\u0430\u0441\u0447\u0435\u0442 \u0438\u0437 \u0420\u0435\u0435\u0441\u0442\u0440\u0430", None))
        self.PBExtract.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0432\u0435\u0441\u0442\u0438 \u0420\u0435\u0435\u0441\u0442\u0440 \u0432 Excel", None))
        self.textEdit_11.setMarkdown(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0447\u0435\u043d\u044c \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u043d\u044b\u0445 \u0440\u0430\u0441\u0447\u0435\u0442\u043e\u0432\n"
"\n"
"", None))
        self.textEdit_11.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:5px; margin-bottom:5px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u041f\u0435\u0440\u0435\u0447\u0435\u043d\u044c \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u043d\u044b\u0445 \u0440\u0430\u0441\u0447\u0435\u0442\u043e\u0432</p></body></html>", None))
        self.textEdit_4.setMarkdown(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435\n"
"\n"
"", None))
        self.textEdit_4.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:5px; margin-bottom:5px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435</p></body></html>", None))
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
        self.textEdit_5.setMarkdown(QCoreApplication.translate("MainWindow", u"\u0410\u0440\u0442\u0438\u043a\u0443\u043b\n"
"\n"
"", None))
        self.textEdit_5.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:5px; margin-bottom:5px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0410\u0440\u0442\u0438\u043a\u0443\u043b</p></body></html>", None))
        self.LEArticul.setInputMask("")
        self.LEArticul.setText("")
        self.LEArticul.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0414\u0435\u0446\u0438\u043c\u0430\u043b\u044c\u043d\u044b\u0439 \u2116", None))
        self.textEdit_6.setMarkdown(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u043c\u0435\u0440 \u043f\u0430\u0440\u0442\u0438\u0438\n"
"\n"
"", None))
        self.textEdit_6.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:5px; margin-bottom:5px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0420\u0430\u0437\u043c\u0435\u0440 \u043f\u0430\u0440\u0442\u0438\u0438</p></body></html>", None))
        self.LEamount.setInputMask("")
        self.LEamount.setText("")
        self.LEamount.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b-\u0432\u043e, \u0448\u0442.", None))
        self.textEdit_8.setMarkdown(QCoreApplication.translate("MainWindow", u"\u041c\u0430\u0440\u043a\u0430 \u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b\u0430\n"
"\n"
"", None))
        self.textEdit_8.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:5px; margin-bottom:5px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u041c\u0430\u0440\u043a\u0430 \u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b\u0430</p></body></html>", None))
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
        self.textEdit_10.setMarkdown(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0440\u043c\u0430 \u0440\u0430\u0441\u0445\u043e\u0434\u0430 \u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b\u0430, \u043a\u0433\n"
"\n"
"", None))
        self.textEdit_10.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:5px; margin-bottom:5px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u041d\u043e\u0440\u043c\u0430 \u0440\u0430\u0441\u0445\u043e\u0434\u0430 \u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b\u0430, \u043a\u0433</p></body></html>", None))
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
        self.LEMaterialrate.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u043a\u0433", None))
        self.textEdit_7.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7.8pt;\">\u041f\u043b\u043e\u0449\u0430\u0434\u044c \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0438, \u043c\u043c2</span></p></body></html>", None))
        self.LEarea.setInputMask("")
        self.LEarea.setText("")
        self.LEarea.setPlaceholderText(QCoreApplication.translate("MainWindow", u"mm2", None))
        self.textEdit_9.setMarkdown(QCoreApplication.translate("MainWindow", u"\u0413\u043b\u0443\u0431\u0438\u043d\u0430 \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0438, \u043c\u043c\n"
"\n"
"", None))
        self.textEdit_9.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:5px; margin-bottom:5px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7.8pt;\">\u0413\u043b\u0443\u0431\u0438\u043d\u0430 \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0438, \u043c\u043c</span></p></body></html>", None))
        self.LEdeep.setText("")
        self.LEdeep.setPlaceholderText(QCoreApplication.translate("MainWindow", u"mm", None))
        self.PBRaschet.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0447\u0438\u0442\u0430\u0442\u044c", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u0440\u0430\u0441\u0447\u0435\u0442", None))
    # retranslateUi

