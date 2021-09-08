import datetime
import xlsxwriter
import sqlite3

con = sqlite3.connect('fieldlist_var2.db')
expenses = []
with con:
    cur = con.cursor()
    cur.execute("SELECT * FROM fieldlist")  # ORDER BY id DESC LIMIT 3
    for row in cur:
        expenses.append(row)
    #print(expenses)

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
worksheet.write('H1', 'Срок изготовления партии,  дней', bold)

# Write some data.
for num_row, row_data in enumerate(expenses):  # expenses
    for num_col, col_data in enumerate(row_data):
        worksheet.write(num_row+1, num_col, col_data)

# Widen the first column to make the text clearer.
#worksheet.set_column('A:A', 20)

# Insert an image.
#worksheet.insert_image('B5', 'logo.png')

workbook.close()
