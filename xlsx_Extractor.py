import datetime
import xlsxwriter
import sqlite3


fieldlist_ = []
work_cost_ = []
connect_to_db = sqlite3.connect('fieldlist_var2.db')
with connect_to_db:
    cursor_fieldlist_ = connect_to_db.cursor()
    cursor_fieldlist_.execute("SELECT * FROM fieldlist")  # ORDER BY id DESC LIMIT 10
    cursor_work_cost_ = connect_to_db.cursor()
    cursor_work_cost_.execute("SELECT time_days FROM work_cost")
    for row in cursor_fieldlist_:
        fieldlist_.append(row)
    for row in cursor_work_cost_:
        work_cost_.append(row)
    print(fieldlist_)
    print(work_cost_)


# Create an new Excel file and add a worksheet.
workbook = xlsxwriter.Workbook('Реестр_' + str(datetime.date.today()) + '.xlsx')
worksheet = workbook.add_worksheet(str(datetime.date.today()))

# Add a bold format to use to highlight cells.
bold = workbook.add_format({'bold': True})

# Write data headers.
worksheet.write('A1', '№ п/п', bold)
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

# Widen the first column to make the text clearer.
#worksheet.set_column('A:A', 20)

# Insert an image.
#worksheet.insert_image('B5', 'logo.png')

workbook.close()
