import tensorflow as tf

# プレースホルダーを定義
a = tf.placeholder(tf.int32, [3]) # 整数型の要素３個の配列

# 配列を２倍にする演算を定義
b = tf.constant(2)
x2_op = a * b

# セッションを開始
sess = tf.Session()

# プレースホルダーに値を当てはめて実行
r1 = sess.run(x2_op, feed_dict={ a:[1, 2, 3] })
print(r1)
r2 = sess.run(x2_op, feed_dict={ a:[10, 20, 30] })
print(r2)
