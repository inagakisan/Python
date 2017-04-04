import codecs

# Shift-JISのCSVファイルを読む
filename = "list-sjis.csv"
csv = codecs.open(filename, "r", encoding="shift-jis").read()

# CSVをPythonのリストに変換する
data = []
rows = csv.split()
for row in rows:
    if row == "":
        continue
    cells = row.split(",")
    data.append(cells)

# 変換結果を表示
for c in data:
    print(c[1], c[2])
