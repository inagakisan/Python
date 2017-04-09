import pandas as pd
from sklearn import svm, metrics, model_selection

# アヤメのCSVデータを読み込む
csv = pd.read_csv('iris.csv')

# 任意の列を取り出す
csv_data = csv[["SepalLength","SepalWidth","PetalLength","PetalWidth"]]
csv_label = csv["Name"]

# 学習用とテスト用に分割する
train_data, test_data, train_label, test_label = model_selection.train_test_split(csv_data, csv_label)

# データを学習し、予測する
clf = svm.SVC()
clf.fit(train_data, train_label)
pre = clf.predict(test_data)

# 正解率を求める
ac_score = metrics.accuracy_score(test_label, pre)
print("正解率＝", ac_score)
