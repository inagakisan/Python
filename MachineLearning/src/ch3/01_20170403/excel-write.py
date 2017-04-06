import openpyxl

# Excelファイルを開く
filename = "population.xlsx"
book = openpyxl.load_workbook(filename)

# アクティブになっているシートを得る
sheet = book.active

# 人口のトータルを計算する
total = 0
for i, row in enumerate(sheet.rows):
    if i == 0:
        continue # 先頭はヘッダ
    po = int(row[3].value)
    total += po
print("total=", total)

# 書き込む
sheet['A49'] = "Total"
sheet['D49'] = total

# フォントなどの設定を変更する
c = sheet['D49']
c.font = openpyxl.styles.Font(size=14, color="FF0000")
c.number_format = sheet['D48'].number_format

# 書き込んだ内容をファイルへ保存
filename = "population-total.xlsx"
book.save(filename)
print("OK")
