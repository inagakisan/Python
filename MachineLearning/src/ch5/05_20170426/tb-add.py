import tensorflow as tf

# 変数や定数を定義
a = tf.constant(100, name="a")
b = tf.constant(200, name="b")
c = tf.constant(300, name="c")
v = tf.Variable(0, name="v")

# 計算を行うグラフを定義
calc_op = a + b * c
assign_op = tf.assign(v, calc_op)

# セッションを作成
sess = tf.Session()

# TensorBoardを使う
tw = tf.summary.FileWriter("log_dir", graph=sess.graph)

# セッションを実行する
sess.run(assign_op)
print(sess.run(v))
