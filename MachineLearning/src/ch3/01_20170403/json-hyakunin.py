import urllib.request as req
import os.path, random
import json

# JSONデータをダウンロード
url = "http://api.aoikujira.com/hyakunin/get.php?fmt=json"
savename = "hyakunin.json"
if not os.path.exists(savename):
    req.urlretrieve(url, savename)

# JSONファイルを解析
data = json.load(open(savename, "r", encoding="utf-8"))
# あるいは・・・
# s = open(savename, "r", encoding="utf-8")
# data = json.load(s)

# ランダムに一首表示
r = random.choice(data)
print(r['kami'], r['simo'])
