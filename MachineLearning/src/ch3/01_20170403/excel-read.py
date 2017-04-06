import openpyxl

# Excelファイルを開く
filename = "population.xlsx"
book = openpyxl.load_workbook(filename)

# 先頭のシートを得る
sheet = book.worksheets[0]

# シートの各業を順に得る
data = []
for row in sheet.rows:
    data.append([
        row[0].value,
        row[3].value
    ])

# 先頭行は説明なので捨てる
del data[0]

# データを人口順に並び替える
data = sorted(data, key=lambda x:x[1])

# ワースト５を表示
for i, a in enumerate(data):
    if (i >= 5):
        break
    print(i+1, a[0], int(a[1]))
