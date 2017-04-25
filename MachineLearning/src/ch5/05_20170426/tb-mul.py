import tensorflow as tf

# データフローグラフを構築
a = tf.constant(20, name="a")
b = tf.constant(30, name="b")
mul_op = a * b

# セッションを生成
sess = tf.Session()

# TensorBoardを使う
tw = tf.summary.FileWriter("log_dir", graph=sess.graph)

# セッションを実行する
print(sess.run(mul_op))
