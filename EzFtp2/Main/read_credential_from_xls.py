import openpyxl

workbook = openpyxl.Workbook(r"D:\D_drive_BACKUP\Study\PycharmProjects\EzFtp2\EzFtp2\Data\credentials.xlsx")
sheet1 = workbook.create_sheet(title="Sheet1")
mc = sheet1.max_column
mr = sheet1.max_row





