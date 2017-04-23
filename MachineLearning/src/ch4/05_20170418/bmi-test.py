from sklearn import model_selection, svm, metrics
import matplotlib.pyplot as plt
import pandas as pd

# 身長・体重データの読み込み
tbl = pd.read_csv("bmi.csv")

# カラム（列）をスライスして正規化
label = tbl["label"]
w = tbl["weight"] / 100 # 最大100kgと考える
h = tbl["height"] / 200 # 最大200cmと考える
wh = pd.concat([w, h], axis=1)

# 学習用とテスト用データに分ける
data_train, data_test, label_train, label_test = model_selection.train_test_split(wh, label)

# データを学習
clf = svm.SVC()
clf.fit(data_train, label_train)

# データを予測
predict = clf.predict(data_test)

# 合っているか結果を確認
ac_score = metrics.accuracy_score(label_test, predict)
cl_report = metrics.classification_report(label_test, predict)
print("正解率=", ac_score)
print("レポート\n", cl_report)
