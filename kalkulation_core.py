from PySide2 import QtCore
import main
import sqlite3


class MyKalkulationCore(QtCore.QThread):
    signalTrudoemkost = QtCore.Signal(str)
    signalSebestoimost = QtCore.Signal(str)
    signalVremyapartii = QtCore.Signal(str)

    def __init__(self, parent=None):
        super(MyKalkulationCore, self).__init__(parent)

    def setParameters(self, naimenovanie, artiсul, amount, area_mm2, deep_mm, material, material_rate):
        self.naimenovanie = naimenovanie
        self.artikul = artiсul
        self.amount = amount
        self.area = area_mm2
        self.deep = deep_mm
        self.material = material
        self.material_rate = material_rate

    def run(self):

        """Реализован поиск цены по сравнению столба material_mark, из БД material_cost, c lineEdit LEMaterial
        :param
        - SetParameters собирает все параметры для математических расчетов
        - LEMaterial для поиска в БД"""

        print("Run !")
        print(self.naimenovanie)
        print(self.artikul)
        print(self.amount)
        print(self.area)
        print(self.deep)
        print(self.material)  # "Лист Д16Ам 1,2х1200х3000" 303rub
        print(self.material_rate)
        #speed = float(self.area) * 1.8  # 1.8 - стандартное время обработки 1мм2
        #skorostsloev = float(self.deep) * speed  # кол-во слоев(1слой=1мм) * Nмм2/сек
        """Трудоёмкость = ((Площадь *1.8 * Глубину) / 3600)
        - 1.8 - стандартное время обработки 1мм2 площади
        - 3600 - кол-во секунд в 1 часе"""
        """Нужна валидация вводимых данных"""
        resultlabour = round(((float(self.area) * 1.8) * float(self.deep)) / 3600, 3)  # трудоемкость = площадь обработки*кол-во секунд / 3600(перевод в н/ч)

        """Поиск цены """
        connect_to_db = sqlite3.connect('fieldlist_var2.db')
        cursor = connect_to_db.cursor()
        cursor.execute('SELECT material_cost_rub FROM material_cost WHERE material_mark LIKE ?', [self.material])
        for row in cursor:
            matprice = round(row[0], 2)
        materialcost = float(self.material_rate) * matprice  # данные из БД material_cost через условие
        resultsebest = round(resultlabour * 2350 + materialcost, 2)  # 2350 =  цена нормочаса в руб. с НДС
        vremyapartii = (float(self.area) * 1.8) * float(self.deep) * float(self.amount) // (3600 * 7.5)
        print(f"Цена материала =  {matprice} руб./кг с НДС")
        print(f"Трудоёмкость {resultlabour} н.ч.")
        print(f"Стоимость материала {materialcost} руб. с НДС")
        print(f"Стоимость работы =  {round(resultlabour * 2350, 2)} руб./кг с НДС")
        print(f"Полная себестоимость {resultsebest} руб. с НДС")
        print(f"Срок изготовления партии {vremyapartii} дней")

        self.signalTrudoemkost.emit(str(resultlabour))
        self.signalSebestoimost.emit(str(resultsebest))
        self.signalVremyapartii.emit(str(vremyapartii))
