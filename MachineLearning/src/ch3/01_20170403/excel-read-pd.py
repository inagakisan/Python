import pandas as pd

# Excelファイルを開く
filename = "population.xlsx"
sheet_name = "Sheet1"
book = pd.read_excel(filename, sheetname=sheet_name)

# データを人口順に表示
book = book.sort_values(by=["２７年"], ascending=False)
print(book)
