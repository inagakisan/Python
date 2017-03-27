# ライブラリ読み込み
import urllib.request

# URLと保存パスを指定
url = "http://uta.pw/shodou/img/28/214.png"
savename = "test.png"

# ダウンロード
urllib.request.urlretrieve(url, savename)
print("保存しました")
