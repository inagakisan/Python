from sklearn import model_selection
from PIL import Image
import os, glob
import numpy as np

# 分類対象のカテゴリを選ぶ
caltech_dir = "../01_20170519/image/101_ObjectCategories"
categories = ["chair","camera","butterfly","elephant","flamingo"]
nb_classes = len(categories)

# 画像サイズを指定
image_w = 64
image_h = 64
pixels = image_w * image_h * 3

# 画像データを読み込み
X = []
Y = []
for idx, cat in enumerate(categories):
    # ラベルを指定
    label = [0 for i in range(nb_classes)]
    label[idx] = 1
    # 画像
    image_dir = caltech_dir + "/" + cat
    files = glob.glob(image_dir + "/*.jpg")
    for i, f in enumerate(files):
        img = Image.open(f)
        img = img.convert("RGB")
        img = img.resize((image_w, image_h))
        data = np.asarray(img)
        X.append(data)
        Y.append(label)
        if i % 10 == 0:
            print(i, "\n", data)
X = np.array(X)
Y = np.array(Y)

# 学習データとテストデータを分ける
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, Y)
xy = (X_train, X_test, y_train, y_test)
np.save("./image/5obj.npy", xy)

print("ok,", len(Y))
