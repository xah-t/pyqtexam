import datetime
import xlsxwriter
import openpyxl
import sqlite3
import os
import subprocess


class Extractor():
    """Класс для вывода Реестра в xlsx файл"""

    def init_tables(self):
        fieldlist_ = []
        work_cost_ = []
        material_cost_ = []
        n_r = 235
        connect_to_db = sqlite3.connect('fieldlist_var2.db')  # fieldlist_var2.db
        with connect_to_db:
            cursor_fieldlist_ = connect_to_db.cursor()
            cursor_fieldlist_.execute("SELECT id, articul, name FROM fieldlist")  # ORDER BY id DESC LIMIT 10
            for row in cursor_fieldlist_:
                fieldlist_.append(row)
            cursor_work_cost_ = connect_to_db.cursor()
            cursor_work_cost_.execute("SELECT labour, work_cost_rub FROM work_cost")
            for row in cursor_work_cost_:
                work_cost_.append(row)
            cursor_material_cost_ = connect_to_db.cursor()
            cursor_material_cost_.execute(f"SELECT work_cost_rub + material_cost_rub * {n_r} AS final_cost FROM work_cost, material_cost")
            # прописать значение н.р. здесь как множитель material_cost, или сначала выгрузить material_cost в переменную, а потом умножить на н.р.??
            for row in cursor_material_cost_:
                material_cost_.append(row)

        # Create an new Excel file and add a worksheet.
        workbook = xlsxwriter.Workbook('Реестр_' + str(datetime.date.today()) + '.xlsx')
        worksheet = workbook.add_worksheet(str(datetime.date.today()))

        # Add a bold format to use to highlight cells.
        bold = workbook.add_format({'bold': True})

        # Write data headers.
        worksheet.write('A1', 'ID', bold)
        worksheet.write('B1', 'Децимальный №', bold)
        worksheet.write('C1', 'Наименование', bold)
        #worksheet.write('D1', 'Площадь поверхности, мм2', bold)
        #worksheet.write('E1', 'Глубина обработки, мм"', bold)
        worksheet.write('D1', 'Трудоемкость, н/ч', bold)
        worksheet.write('E1', 'Стоимость работ, руб. с НДС', bold)
        worksheet.write('F1', 'Стоимость материала, руб. с НДС', bold)
        #worksheet.write('H1', 'Срок изготовления партии,  дней', bold)  #нужно взять из другой таблицы

        # Write some data.
        for num_row, row_data in enumerate(fieldlist_):  # expenses
            for num_col, col_data in enumerate(row_data):
                worksheet.write(num_row+1, num_col, col_data)
        for num_row, row_data in enumerate(work_cost_):
            for num_col, col_data in enumerate(row_data):
                worksheet.write(num_row+1, num_col+3, col_data)
        for num_row, row_data in enumerate(material_cost_):
            for num_col, col_data in enumerate(row_data):
                worksheet.write(num_row+1, num_col+5, col_data)
        return workbook

    def close(self):
        self.workbook = self.init_tables()
        self.workbook.close()

    def show(self):
        self.path = "C:/python/VKR/pyqtexam/Реестр_" + str(datetime.date.today()) + ".xlsx"
        subprocess.Popen(self.path, shell=True)


def download_catalog(path):

    """Функция загрузки прайса на матераил в БД"""

    values_ = []
    wb_obj = openpyxl.load_workbook(path)
    sheet_obj = wb_obj.active
    connect_to_db = sqlite3.connect('fieldlist_var2.db')
    cursor_material_cost_ = connect_to_db.cursor()
    for i in range(1, sheet_obj.max_row):
        cell_obj = sheet_obj.cell(row=i, column=1)
        cell_obj_1 = sheet_obj.cell(row=i, column=2)
        values_.append(cell_obj.value)
        values_.append(cell_obj_1.value)
        #print(values_)
        sql_ = "insert into material_cost (material_mark, material_cost_rub) values(?, ?)"
        cursor_material_cost_.execute(sql_, values_)
        values_ = []
    #connect_to_db.commit()


if __name__ == '__main__':
    upload_ = Extractor()
    upload_.init_tables()
    upload_.show()
    path = 'C:/python/VKR/pyqtexam/material_catalog.xlsx'
    download_catalog(path)
