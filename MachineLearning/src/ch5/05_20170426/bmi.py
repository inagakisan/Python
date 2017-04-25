import pandas as pd
import numpy as np
import tensorflow as tf

# 身長、体重、ラベルのCSVデータを読み出す
csv = pd.read_csv("../../ch4/05_20170418/bmi.csv")
# データを正規化
csv["height"] = csv["height"] / 200
csv["weight"] = csv["weight"] / 100
# ラベルを三次元のクラスで表す
# - thin=(1,0,0) / normal=(0,1,0) / fat=(0,0,1)
bclass = {"thin": [1,0,0], "normal": [0,1,0], "fat": [0,0,1]}
csv["label_pat"] = csv["label"].apply(lambda x: np.array(bclass[x]))

# 正解率を求めるためにテストデータを準備
test_csv = csv[15000:20000]
test_pat = test_csv[["weight","height"]]
test_ans = list(test_csv["label_pat"])

# データフローグラフを構築する
# データを入れるプレースホルダを宣言
x  = tf.placeholder(tf.float32, [None, 2], name="x") # 身長、体重のデータを入れる
y_ = tf.placeholder(tf.float32, [None, 3], name="y_") # 答えのラベルを入れる

# interfaceの部分をスコープにまとめる
with tf.name_scope('interface') as scope:
    W = tf.Variable(tf.zeros([2, 3]), name="W") # 重み
    b = tf.Variable(tf.zeros([3]), name="b") # バイアス
    # ソフトマックス回帰を定義
    with tf.name_scope('softmax') as scope:
        y = tf.nn.softmax(tf.matmul(x, W) + b)

# lossの計算をスコープにまとめる
with tf.name_scope('loss') as scope:
    cross_entropy = -tf.reduce_sum(y_ * tf.log(y))

# trainingの計算をスコープにまとめる
with tf.name_scope('training') as scope:
    optimizer = tf.train.GradientDescentOptimizer(0.01)
    train = optimizer.minimize(cross_entropy)

# accuracyの計算をスコープにまとめる
with tf.name_scope('accuracy') as scope:
    predict = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
    accuracy = tf.reduce_mean(tf.cast(predict, tf.float32))

# セッションを開始
sess = tf.Session()
sess.run(tf.global_variables_initializer()) # 変数を初期化
# テストデータを用いて学習させる
for step in range(3500):
    i = (step * 100) % 14000
    rows = csv[1 + i : 1 + i + 100]
    x_pat = rows[["weight","height"]]
    y_ans = list(rows["label_pat"])
    fd = {x: x_pat, y_: y_ans}
    sess.run(train, feed_dict=fd)
    if step % 500 == 0:
        cre = sess.run(cross_entropy, feed_dict=fd)
        acc = sess.run(accuracy, feed_dict={x: test_pat, y_: test_ans})
        print("step=", step, "cre=", cre, "acc=", acc)

# 最終的な正解率を求める
acc = sess.run(accuracy, feed_dict={x: test_pat, y_: test_ans})
print("正解率＝", acc)

# TensorBoardを使う
tf.summary.FileWriter("log_dir", graph=sess.graph)
