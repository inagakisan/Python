from bs4 import BeautifulSoup
import urllib.request as req

url = "http://api.aoikujira.com/zip/xml/1500042"

# urlopen()でデータを取得
res = req.urlopen(url)

# BeautifulSoupで解析
soup = BeautifulSoup(res, "html.parser")

# 任意のデータを抽出
ken = soup.find("ken").string
shi = soup.find("shi").string
cho = soup.find("cho").string
print(ken, shi, cho)
