import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn import model_selection, metrics

# データの読み込み
mr = pd.read_csv("mushroom.csv", header=None)

# データ中の記号を数値に変換する
label = []
data = []
attr_list =[]
for row_index, row in mr.iterrows():
    label.append(row.ix[0])
    row_data = []
    for v in row.ix[1:]:
        row_data.append(ord(v))
    data.append(row_data)

# 学習用データとテスト用データに分ける
data_train, data_test, label_train, label_test = model_selection.train_test_split(data, label)

# データの学習
clf = RandomForestClassifier()
clf.fit(data_train, label_train)

# データを予測
predict = clf.predict(data_test)

# 合っているか結果を確認
ac_score = metrics.accuracy_score(label_test, predict)
cl_report = metrics.classification_report(label_test, predict)
print("正解率＝", ac_score)
print("レポート＝\n", cl_report)
