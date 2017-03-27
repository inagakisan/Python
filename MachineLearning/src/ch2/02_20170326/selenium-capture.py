from selenium import webdriver

url = "http://www.aozora.gr.jp/cards/000081/files/46268_23911.html"

# PhantomJSのドライバを得る
browser = webdriver.PhantomJS()
# 暗黙的な待機を最大３秒行う
browser.implicitly_wait(3)
# URLを読み込む
browser.get(url)
# 画面をキャプチャしてファイルに保存
browser.save_screenshot("Website.png")
# ブラウザーを終了
browser.quit()
