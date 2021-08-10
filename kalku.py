# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'kalkulation.ui'
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
        MainWindow.resize(879, 663)
        MainWindow.setMinimumSize(QSize(0, 0))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(50, 20, 771, 61))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.TENaimenovanie = QTextEdit(self.layoutWidget)
        self.TENaimenovanie.setObjectName(u"textEdit_4")
        self.TENaimenovanie.setEnabled(False)
        self.TENaimenovanie.setReadOnly(True)

        self.verticalLayout_4.addWidget(self.TENaimenovanie)

        self.LENaimenovanie = QLineEdit(self.layoutWidget)
        self.LENaimenovanie.setObjectName(u"lineEdit_1")

        self.verticalLayout_4.addWidget(self.LENaimenovanie)


        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.TEArticul = QTextEdit(self.layoutWidget)
        self.TEArticul.setObjectName(u"textEdit_5")
        self.TEArticul.setEnabled(False)
        self.TEArticul.setReadOnly(True)

        self.verticalLayout_5.addWidget(self.TEArticul)

        self.LEArticul = QLineEdit(self.layoutWidget)
        self.LEArticul.setObjectName(u"lineEdit_2")

        self.verticalLayout_5.addWidget(self.LEArticul)


        self.horizontalLayout.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.TEKolichestvo = QTextEdit(self.layoutWidget)
        self.TEKolichestvo.setObjectName(u"textEdit_6")
        self.TEKolichestvo.setEnabled(False)
        self.TEKolichestvo.setReadOnly(True)

        self.verticalLayout_6.addWidget(self.TEKolichestvo)

        self.LEKolichestvo = QLineEdit(self.layoutWidget)
        self.LEKolichestvo.setObjectName(u"lineEdit_3")
        self.LEKolichestvo.setMaximumSize(QSize(300, 16777215))

        self.verticalLayout_6.addWidget(self.LEKolichestvo)


        self.horizontalLayout.addLayout(self.verticalLayout_6)

        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(50, 200, 771, 61))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.TETrudoemkost = QTextEdit(self.layoutWidget1)
        self.TETrudoemkost.setObjectName(u"textEdit")
        self.TETrudoemkost.setEnabled(False)
        self.TETrudoemkost.setReadOnly(True)

        self.verticalLayout.addWidget(self.TETrudoemkost)

        self.LETrudoemkost = QLineEdit(self.layoutWidget1)
        self.LETrudoemkost.setObjectName(u"lineEdit_6_Trudoemkost")

        self.verticalLayout.addWidget(self.LETrudoemkost)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.TESebestoimost = QTextEdit(self.layoutWidget1)
        self.TESebestoimost.setObjectName(u"textEdit_2")
        self.TESebestoimost.setEnabled(False)
        self.TESebestoimost.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.TESebestoimost)

        self.LESebestoimost = QLineEdit(self.layoutWidget1)
        self.LESebestoimost.setObjectName(u"lineEdit_7_Sebestoimost")

        self.verticalLayout_2.addWidget(self.LESebestoimost)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.TEVremyapartii = QTextEdit(self.layoutWidget1)
        self.TEVremyapartii.setObjectName(u"textEdit_3")
        self.TEVremyapartii.setEnabled(False)
        self.TEVremyapartii.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.TEVremyapartii)

        self.LEVremyapartii = QLineEdit(self.layoutWidget1)
        self.LEVremyapartii.setObjectName(u"lineEdit_8_Vremyapartii")

        self.verticalLayout_3.addWidget(self.LEVremyapartii)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

        self.layoutWidget2 = QWidget(self.centralwidget)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(50, 560, 771, 30))
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.PBSaved = QPushButton(self.layoutWidget2)
        self.PBSaved.setObjectName(u"PBSaved")

        self.horizontalLayout_4.addWidget(self.PBSaved)

        self.PBMoved = QPushButton(self.layoutWidget2)
        self.PBMoved.setObjectName(u"PBMoved")

        self.horizontalLayout_4.addWidget(self.PBMoved)

        self.layoutWidget3 = QWidget(self.centralwidget)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(70, 100, 711, 61))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.TEPloshad = QTextEdit(self.layoutWidget3)
        self.TEPloshad.setObjectName(u"textEdit_7")
        self.TEPloshad.setEnabled(False)
        self.TEPloshad.setReadOnly(True)

        self.verticalLayout_7.addWidget(self.TEPloshad)

        self.LEPloshad = QLineEdit(self.layoutWidget3)
        self.LEPloshad.setObjectName(u"lineEdit_4")
        self.LEPloshad.setMinimumSize(QSize(200, 0))
        self.LEPloshad.setMaximumSize(QSize(200, 16777215))

        self.verticalLayout_7.addWidget(self.LEPloshad)


        self.horizontalLayout_2.addLayout(self.verticalLayout_7)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.TEGlubina = QTextEdit(self.layoutWidget3)
        self.TEGlubina.setObjectName(u"textEdit_9")
        self.TEGlubina.setEnabled(False)
        self.TEGlubina.setReadOnly(True)

        self.verticalLayout_8.addWidget(self.TEGlubina)

        self.LEGlubina = QLineEdit(self.layoutWidget3)
        self.LEGlubina.setObjectName(u"lineEdit_5_Glubina")
        self.LEGlubina.setMinimumSize(QSize(200, 0))
        self.LEGlubina.setMaximumSize(QSize(200, 16777215))

        self.verticalLayout_8.addWidget(self.LEGlubina)


        self.horizontalLayout_2.addLayout(self.verticalLayout_8)

        self.PBRaschet = QPushButton(self.layoutWidget3)
        self.PBRaschet.setObjectName(u"PBRaschet")
        self.PBRaschet.setMinimumSize(QSize(70, 59))
        self.PBRaschet.setMaximumSize(QSize(300, 16777215))

        self.horizontalLayout_2.addWidget(self.PBRaschet)

        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(50, 280, 769, 261))
        self.tableView.setMaximumSize(QSize(16777215, 300))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 879, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.TENaimenovanie.setHtml(QCoreApplication.translate("MainWindow", u"Наименование детали", None))
#if QT_CONFIG(tooltip)
        self.LENaimenovanie.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.LENaimenovanie.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.LENaimenovanie.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.LENaimenovanie.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.LENaimenovanie.setInputMask("")
        self.LENaimenovanie.setText("")
        self.LENaimenovanie.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u0434\u0435\u0442\u0430\u043b\u0438", None))
        self.TEArticul.setHtml(QCoreApplication.translate("MainWindow", u"Децимальный №", None))
        self.LEArticul.setInputMask("")
        self.LEArticul.setText("")
        self.LEArticul.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Введите децимальный №", None))
        self.TEKolichestvo.setHtml(QCoreApplication.translate("MainWindow", u"Объем партии, шт.", None))
        self.LEKolichestvo.setInputMask("")
        self.LEKolichestvo.setText("")
        self.LEKolichestvo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b-\u0432\u043e, \u0448\u0442.", None))
        self.TETrudoemkost.setHtml(QCoreApplication.translate("MainWindow", u"Трудоемкость, н/ч", None))
        self.LETrudoemkost.setInputMask("")
        self.LETrudoemkost.setText("")
        self.LETrudoemkost.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u043d/\u0447", None))
        self.TESebestoimost.setHtml(QCoreApplication.translate("MainWindow", u"Себестоимость детали, руб. с НДС", None))
        self.LESebestoimost.setInputMask("")
        self.LESebestoimost.setText("")
        self.LESebestoimost.setPlaceholderText(QCoreApplication.translate("MainWindow", u"руб. с НДС", None))
        self.TEVremyapartii.setHtml(QCoreApplication.translate("MainWindow", u"Срок изготовления партии, часов", None))
        self.LEVremyapartii.setText("")
        self.LEVremyapartii.setPlaceholderText(QCoreApplication.translate("MainWindow", u"часов", None))
        self.PBSaved.setText(QCoreApplication.translate("MainWindow", u"Сохранить расчет в Реестр", None))
        self.PBMoved.setText(QCoreApplication.translate("MainWindow", u"Удалить расчет из Реестра", None))
        self.TEPloshad.setHtml(QCoreApplication.translate("MainWindow", u"Площадь обрабатываемой поверхности, мм2", None))
        self.LEPloshad.setInputMask("")
        self.LEPloshad.setText("")
        self.LEPloshad.setPlaceholderText(QCoreApplication.translate("MainWindow", u"mm2", None))
        self.TEGlubina.setMarkdown(QCoreApplication.translate("MainWindow", u"\u0413\u043b\u0443\u0431\u0438\u043d\u0430 \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0438, \u043c\u043c\n"
"\n"
"", None))
        self.TEGlubina.setHtml(QCoreApplication.translate("MainWindow", u"Глубина обрабатываемой поверхности, мм", None))
        self.LEGlubina.setText("")
        self.LEGlubina.setPlaceholderText(QCoreApplication.translate("MainWindow", u"mm", None))
        self.PBRaschet.setText(QCoreApplication.translate("MainWindow", u"Расчитать!", None))
    # retranslateUi

