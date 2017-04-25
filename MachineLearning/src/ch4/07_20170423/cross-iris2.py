import pandas as pd
from sklearn import svm, metrics, model_selection
import random, re

# アヤメのCSVデータを読み込む
csv = pd.read_csv("../02_20170408/iris.csv")

# リストを訓練データとラベルに分割する
data = csv[["SepalLength","SepalWidth","PetalLength","PetalWidth"]]
label = csv["Name"]

# クロスバリデーションを行う
clf = svm.SVC()
scores = model_selection.cross_val_score(clf, data, label, cv=5)
print("各正解率＝", scores)
print("平均正解率＝", scores.mean())
