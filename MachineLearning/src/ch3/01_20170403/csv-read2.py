import csv, codecs

# Shift-JISのCSVファイルを読む
filename = "list-sjis.csv"
fp = codecs.open(filename, "r", encoding="shift-jis")

# 1行ずつ読む
reader = csv.reader(fp, delimiter=",", quotechar='"')
for c in reader:
    print(c[1], c[2])
