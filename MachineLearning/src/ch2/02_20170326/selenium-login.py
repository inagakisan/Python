from selenium import webdriver

USER = "JS-TESTER"
PASS = "ipCU12ySxI"

# PhantomJSのドライバーを得る
browser = webdriver.PhantomJS()
browser.implicitly_wait(3)

# ログインページにアクセス
url_login = "http://uta.pw/sakusibbs/users.php?action=login"
browser.get(url_login)
print("ログインページにアクセスしました")

# テキストボックスに文字を入力
e = browser.find_element_by_id("user")
e.clear()
e.send_keys(USER)
e = browser.find_element_by_id("pass")
e.clear()
e.send_keys(PASS)
# フォームを送信
frm = browser.find_element_by_css_selector("#loginForm form")
frm.submit()
print("情報を入力してログインボタンを押しました")

# マイページのURLを得る
a = browser.find_element_by_css_selector(".islogin a")
url_mypage = a.get_attribute('href')
print("マイページのURL＝", url_mypage)

# マイページの表示
browser.get(url_mypage)

# お気に入りのタイトルを列挙
links = browser.find_elements_by_css_selector("#favlist li > a")
for a in links:
    href = a.get_attribute('href')
    title = a.text
    print("-", title, ">", href)
