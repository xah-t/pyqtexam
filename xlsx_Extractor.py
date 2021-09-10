import datetime
import xlsxwriter
import sqlite3
import os
import subprocess


class Extractor():
    """Класс для вывода Реестра в xlsx файл"""

    def init_tables(self):
        fieldlist_ = []
        work_cost_ = []
        connect_to_db = sqlite3.connect('fieldlist_var2.db')  # fieldlist_var2.db
        with connect_to_db:
            cursor_fieldlist_ = connect_to_db.cursor()
            cursor_fieldlist_.execute("SELECT * FROM fieldlist")  # ORDER BY id DESC LIMIT 10
            cursor_work_cost_ = connect_to_db.cursor()
            cursor_work_cost_.execute("SELECT time_days FROM work_cost")
            for row in cursor_fieldlist_:
                fieldlist_.append(row)
            for row in cursor_work_cost_:
                work_cost_.append(row)

        # Create an new Excel file and add a worksheet.
        workbook = xlsxwriter.Workbook('Реестр_' + str(datetime.date.today()) + '.xlsx')
        worksheet = workbook.add_worksheet(str(datetime.date.today()))

        # Add a bold format to use to highlight cells.
        bold = workbook.add_format({'bold': True})

        # Write data headers.
        worksheet.write('A1', 'ID', bold)
        worksheet.write('B1', 'Децимальный №', bold)
        worksheet.write('C1', 'Наименование', bold)
        worksheet.write('D1', 'Площадь поверхности, мм2', bold)
        worksheet.write('E1', 'Глубина обработки, мм"', bold)
        worksheet.write('F1', 'Трудоемкость, н/ч', bold)
        worksheet.write('G1', 'Себестоимость, руб. с НДС', bold)
        worksheet.write('H1', 'Срок изготовления партии,  дней', bold)  #нужно взять из другой таблицы

        # Write some data.
        for num_row, row_data in enumerate(fieldlist_):  # expenses
            for num_col, col_data in enumerate(row_data):
                worksheet.write(num_row+1, num_col, col_data)
        for num_row, row_data in enumerate(work_cost_):
            for num_col, col_data in enumerate(row_data):
                worksheet.write(num_row+1, num_col+7, col_data)
        return workbook

    def close(self):
        self.workbook = self.init_tables()
        self.workbook.close()

    def show(self):
        self.path = "C:/python/VKR/pyqtexam/Реестр_" + str(datetime.date.today()) + ".xlsx"
        subprocess.Popen(self.path, shell=True)


if __name__ == '__main__':
    upload_ = Extractor()
    upload_.init_tables()
    #upload_.close()
    upload_.show()
