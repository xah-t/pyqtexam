import datetime
import xlsxwriter


expenses = (
    ['rgrty4557', "shina", 23.55, 245.6, 6],
    ['Gas245', 'opora', 2.54, 300.54, 13],
    ['Fo345od', "Palka", 1.234, 23535, 28],
    ['G13ym', "srert", 13, 45.36, 6],
    ['er45od', "Pachka", 1.2, 25, 2]
)
# Create an new Excel file and add a worksheet.
workbook = xlsxwriter.Workbook('Реестр_' + str(datetime.date.today()) + '.xlsx')
worksheet = workbook.add_worksheet(str(datetime.date.today()))

# Add a bold format to use to highlight cells.
bold = workbook.add_format({'bold': True})

# Write some data headers.
worksheet.write('A1', 'Децимальный №', bold)
worksheet.write('B1', 'Наименование', bold)
worksheet.write('C1', 'Трудоемкость, н/ч', bold)
worksheet.write('D1', 'Себестоимость, руб. с НДС', bold)
worksheet.write('E1', 'Срок изготовления партии,  дней', bold)

row = 1
col = 0
for articul, naimenovanie, trudoemkost, sebestoimost, vremyapartii in (fieldlist):
    worksheet.write(row, col, articul)
    worksheet.write(row, col + 1, naimenovanie)
    worksheet.write(row, col + 2, trudoemkost)
    worksheet.write(row, col + 3, sebestoimost)
    worksheet.write(row, col + 4, vremyapartii)
    row += 1
for row in range(0, 5):
    worksheet.write(row+7, 0, 'Hello')
# Widen the first column to make the text clearer.
#worksheet.set_column('A:A', 20)

# Write some simple text.
#worksheet.write('A1', 'Hello', bold)

# Text with formatting.
#worksheet.write('A2', 'World', bold)

# Write some numbers, with row/column notation.
#worksheet.write(2, 0, 123)
#worksheet.write(3, 0, 123.456)

# Insert an image.
#worksheet.insert_image('B5', 'logo.png')

workbook.close()
