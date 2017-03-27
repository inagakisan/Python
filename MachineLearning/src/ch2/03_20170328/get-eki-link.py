# ライブラリの読み込み
from bs4 import BeautifulSoup

# 解析対象となるHTMLを読み込む
html = open("eki-link.html", encoding="utf-8").read()

# HTMLを解析する
soup = BeautifulSoup(html, "html.parser")

# <a>タグを抽出する
links = soup.select("a[href]")

# （タイトル、URL）のリストを作る
result = []
for a in links:
    href = a.attrs["href"]
    title = a.text
    result.append((title, href))

print(result)
