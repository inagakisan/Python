# TensorFlowを取り込む
import tensorflow as tf

# 定数を定義
a = tf.constant(2)
b = tf.constant(3)
c = tf.constant(4)

# 演算を定義
calc1_op = a + b * c
calc2_op = (a + b) * c

# セッションを開始する
sess = tf.Session()
res1 = sess.run(calc1_op)
print(res1)
res2 = sess.run(calc2_op)
print(res2)
