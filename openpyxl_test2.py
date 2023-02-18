import openpyxl
import random
import time

# 新しいExcelファイルを作成する
workbook = openpyxl.Workbook()

# デフォルトのSheet1を取得する
sheet = workbook.active

# セルに値を書き込む
for i in range(100):
    random_n = random.random()
    cell = sheet.cell(row=i+1, column=1, value=random_n)
    print(random_n)
    time.sleep(0.1)
    

# Excelファイルを保存する
workbook.save('example.xlsx')
workbook.close()
