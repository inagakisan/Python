from bs4 import BeautifulSoup
fp = open("fruits-vegetables.html", encoding="utf-8")
soup = BeautifulSoup(fp, "html.parser")

# CSSセレクタで選び出す
print(soup.select_one("li:nth-of-type(8)").string)
print(soup.select_one("#ve-list > li:nth-of-type(4)").string)
print(soup.select("#ve-list > li[data-lo='us']")[1].string)
print(soup.select("#ve-list > li.black")[1].string)

# findメソッドで選び出す
cond = {
    "data-lo":"us",
    "class":"black"
}
print(soup.find("li", cond).string)

# findを二度組み合わせる
print(soup.find(id="ve-list")
          .find("li",cond).string)
