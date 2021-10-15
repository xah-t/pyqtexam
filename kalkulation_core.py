from PySide2 import QtCore
import main
import sqlite3


class MyKalkulationCore(QtCore.QThread):
    signallabour = QtCore.Signal(str)
    signalprimecost = QtCore.Signal(str)
    signalproductiontime = QtCore.Signal(str)

    def __init__(self, parent=None):
        super(MyKalkulationCore, self).__init__(parent)

    def setParameters(self, name, artiсul, amount, area_mm2, deep_mm, material, material_rate):
        self.name = name
        self.articul = artiсul
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
        print(self.name)
        print(self.articul)
        print(self.amount)
        print(self.area)
        print(self.deep)
        print(self.material)  # "Лист Д16Ам 1,2х1200х3000" 303rub
        print(self.material_rate)

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
        productiontime = (float(self.area) * 1.8) * float(self.deep) * float(self.amount) // (3600 * 7.5)
        print(f"Цена материала =  {matprice} руб./кг с НДС")
        print(f"Трудоёмкость {resultlabour} н.ч.")
        print(f"Стоимость материала {materialcost} руб. с НДС")
        print(f"Стоимость работы =  {round(resultlabour * 2350, 2)} руб./кг с НДС")
        print(f"Полная себестоимость {resultsebest} руб. с НДС")
        print(f"Срок изготовления партии {productiontime} дней")

        self.signallabour.emit(str(resultlabour))
        self.signalprimecost.emit(str(resultsebest))
        self.signalproductiontime.emit(str(productiontime))
