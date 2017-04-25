# TensorFlowを取り込む
import tensorflow as tf

# 定数を定義
a = tf.constant(1234)
b = tf.constant(5000)

# 演算を定義
add_op = a + b

# セッションを開始する
sess = tf.Session()
res = sess.run(add_op)
print(res)
