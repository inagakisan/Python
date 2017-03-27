#!/usr/bin/env python3

# ライブラリの読み込み
import sys
import urllib.request as req
import urllib.parse as parse

# コマンドライン引数を得る
if len(sys.argv) <= 1:
    print("USAGE: hyakunin.py (keyword)")
    sys.exit()
keyword = sys.argv[1]

# パラメータをURLエンコードする
API = "http://api.aoikujira.com/hyakunin/get.php"
query = {
    "fmt": "ini",
    "key": keyword
}
params = parse.urlencode(query)
url = API + "?" + params
print("url=", url)

# ダウンロード
with req.urlopen(url) as r:
    b = r.read()
    data = b.decode('utf-8')
    print(data)
