from PySide2 import QtCore
import main


class MyKalkulationCore(QtCore.QThread):
    signalTrudoemkost = QtCore.Signal(str)
    signalSebestoimost = QtCore.Signal(str)
    signalVremyapartii = QtCore.Signal(str)

    def __init__(self, parent=None):
        super(MyKalkulationCore, self).__init__(parent)

    def setParameters(self, naimenovanie, artikul, kolichestvo, area_mm2, deep_mm, material, material_rate):
        self.naimenovanie = naimenovanie
        self.artikul = artikul
        self.kolichestvo = kolichestvo
        self.ploshad = area_mm2
        self.glubina = deep_mm
        self.material = material
        self.material_rate = material_rate
        """Добавить параметры материала и """
    def run(self):
        print("Run !")
        print(self.naimenovanie)
        print(self.artikul)
        print(self.kolichestvo)
        print(self.ploshad)
        print(self.glubina)
        print(self.material)
        print(self.material_rate)
        skorost = float(self.ploshad) * 1.8  # 1.8 - стандартное время обработки 1мм2
        skorostsloev = float(self.glubina) * skorost  # кол-во слоев * Nмм2/сек
        resultTrud = round(skorostsloev / 3600, 3)  # трудоемкость = площадь обработки*кол-во секунд / 3600(перевод в н/ч)
        """Вставить поиск цены по сравнению столбца material_mark из БД material_cost с LEMaterial"""
        """myinput = main.KalkulationWindow.setLineEditMaterial(text)
        # print(myinput)
        matcost = connect_to_db.cursor()
        matcost = connect_to_db.execute('SELECT material_cost_rub FROM material_cost WHERE material_mark LIKE ?',
                                        [myinput])
        # for row in matcost:
        #     work_cost_.append(row)
        # print(f"выбран материала" + {work_cost_} + ".")
"""
        materialcost = float(self.material_rate) * 645  # вставить вместо 655 (цена за кг) данные из БД material_cost через условие
        print(f"Стоимость материала {materialcost}")
        resultSebest = round(resultTrud * 2350 + materialcost, 2)  # 2350 =  цена нормочаса в руб. с НДС
        vremyapartii = skorostsloev * float(self.kolichestvo) // (3600*7.5)
        print(f"Трудоёмкость {resultTrud}")
        print(f"Себестоимость {resultSebest}")
        print(f"Время обработки партии {vremyapartii} дней")

        self.signalTrudoemkost.emit(str(resultTrud))
        self.signalSebestoimost.emit(str(resultSebest))
        self.signalVremyapartii.emit(str(vremyapartii))
