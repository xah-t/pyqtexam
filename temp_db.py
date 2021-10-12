import datetime
import xlsxwriter
import sqlite3
import openpyxl
from xlrd import open_workbook
import subprocess


fieldlist_ = []
work_cost_ = []
material_cost_ = []
material_dict = {}
values_ = []

path = 'C:/python/VKR/pyqtexam/material_catalog.xlsx'
wb_obj = openpyxl.load_workbook(path)
sheet_obj = wb_obj.active
num_row = 0
connect_to_db = sqlite3.connect('fieldlist_var2.db')
cursor_material_cost_ = connect_to_db.cursor()
for i in range(1, sheet_obj.max_row):
    #for j in range(1, sheet_obj.max_row):
    cell_obj = sheet_obj.cell(row=i, column=1)
    cell_obj_1 = sheet_obj.cell(row=i, column=2)
    values_.append(cell_obj.value)
    values_.append(cell_obj_1.value)  # добавление элемента в конец,
    print(values_)
    sql_ = "insert into material_cost (material_mark, material_cost_rub) values(?, ?)"
    cursor_material_cost_.execute(sql_, values_)
    values_ = []
    num_row += 1
connect_to_db.commit()
print(values_)
"""
connect_to_db = sqlite3.connect('fieldlist_var2.db')
cursor_material_cost_ = connect_to_db.cursor()
for i in range(1, num_row):  # len(list(values_))
    sql_ = "insert into material_cost (material_mark, material_cost_rub) values(?, ?)"
    #values_ = ["J23", 296]
    cursor_material_cost_.execute(sql_, values_)  # cursor_material_cost_.execute("insert into material_cost (material_mark, material_cost_rub) values ('Д16', 275), ('Д16т', 295)")
connect_to_db.commit()"""
cursor_material_cost_.execute("SELECT * FROM material_cost")
for row in cursor_material_cost_:
    material_cost_.append(row)
print(material_cost_)
# with connect_to_db:
#     cursor_fieldlist_ = connect_to_db.cursor()
#     cursor_fieldlist_.execute("SELECT * FROM fieldlist")  # ORDER BY id DESC LIMIT 10
#     cursor_work_cost_ = connect_to_db.cursor()
#     cursor_work_cost_.execute("SELECT time_days FROM work_cost")
#     for row in cursor_fieldlist_:
#         fieldlist_.append(row)
#     for row in cursor_work_cost_:
#         work_cost_.append(row)
#     print(fieldlist_)
#     print(work_cost_)