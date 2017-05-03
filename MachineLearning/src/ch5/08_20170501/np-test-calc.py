import numpy as np

# 10個のfloat32型の０データを生成
v = np.zeros(10, dtype=np.float32)
print(v)

# 連番で10個のunit64型のデータを生成
v = np.arange(10, dtype=np.uint64)
print(v)

# vの値を３倍する
v *= 3
print(v)

# vの平均値を求める
print(v.mean())
