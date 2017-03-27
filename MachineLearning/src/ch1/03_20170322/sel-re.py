from bs4 import BeautifulSoup
import re # 正規表現を使うとき

html = """
<ul>
    <li><a href="hoge.html">hoge</a></li>
    <li><a href="https://example.com/fuga">fuga*</a></li>
    <li><a href="https://example.com/foo">foo*</a></li>
    <li><a href="http://example.com/aaa">aaa</a></li>
</ul>
"""

soup = BeautifulSoup(html, "html.parser")
# 正規表現でhrefからhttpsのものを抽出
li = soup.find_all(href=re.compile(r"^https://"))
for e in li:
    print(e.attrs['href'])
