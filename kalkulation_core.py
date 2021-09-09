from PySide2 import QtCore


class MyKalkulationCore(QtCore.QThread):
    signalTrudoemkost = QtCore.Signal(str)
    signalSebestoimost = QtCore.Signal(str)
    signalVremyapartii = QtCore.Signal(str)

    def __init__(self, parent=None):
        super(MyKalkulationCore, self).__init__(parent)

    def setParameters(self, naimenovanie, artikul, kolichestvo, ploshad, glubina):
        self.naimenovanie = naimenovanie
        self.artikul = artikul
        self.kolichestvo = kolichestvo
        self.ploshad = ploshad
        self.glubina = glubina
        """Добавить параметры материала и """
    def run(self):
        print("Run !")
        print(self.naimenovanie)
        print(self.artikul)
        print(self.kolichestvo)
        print(self.ploshad)
        print(self.glubina)
        skorost = int(self.ploshad) * 1.8  # 1.8 - стандартное время обработки 1мм2
        skorostsloev = int(self.glubina) * skorost  # кол-во слоев * Nмм2/сек
        resultTrud = skorostsloev / 3600  # трудоемкость = площадь обработки*кол-во секунт / 3600(перевод в н/ч)
        resultSebest = resultTrud * 2350  # в дальнейшем - вписать ссылку на lineEdit с ценой нормочаса
        vremyapartii = skorostsloev * int(self.kolichestvo) / 3600
        print(f"Трудоёмкость {resultTrud}")
        print(f"Себестоимость {resultSebest}")
        print(f"Время обработки партии {vremyapartii} часов")

        self.signalTrudoemkost.emit(str(resultTrud))
        self.signalSebestoimost.emit(str(resultSebest))
        self.signalVremyapartii.emit(str(vremyapartii))
