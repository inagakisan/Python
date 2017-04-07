import sqlite3

# sqliteのデータベースに接続
dbpath = "test.sqlite"
conn = sqlite3.connect(dbpath)

# テーブルを作成し、データを挿入する
cur = conn.cursor()
cur.executescript("""
/* itemsテーブルがすでにあれば削除する */
DROP TABLE IF EXISTS items;

/* テーブルの作成 */
CREATE TABLE items(
    item_id INTEGER PRIMARY KEY,
    name TEXT UNIQUE,
    price INTEGER
);

/* データを挿入 */
INSERT INTO items(name, price)VALUES('Apple', 800);
INSERT INTO items(name, price)VALUES('Orange', 780);
INSERT INTO items(name, price)VALUES('Banana', 430);
"""
)
# 上記の操作をデータベースに反映させる
conn.commit()

# データを抽出する
cur = conn.cursor()
cur.execute("SELECT item_id, name, price FROM items;")
item_list = cur.fetchall()

# 1行ずつ表示
for it in item_list:
    print(it)
