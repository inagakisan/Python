from sklearn import svm, metrics
import glob, os.path, re, json

# テキストを読んで出現頻度を調べる
def check_freq(fname):
    name = os.path.basename(fname)
    lang = re.match(r'^[a-z]{2,}', name).group()
    with open(fname, "r", encoding="utf-8") as f:
        text = f.read()
    text = text.lower() # 小文字に変換
    # カウンタを０に
    cnt = [0 for n in range(0, 26)]
    code_a = ord("a")
    code_z = ord("z")
    # アルフェベットの出現回数を調べる
    for ch in text:
        n = ord(ch)
        if code_a <= n <= code_z: # a-zの間なら
            cnt[n - code_a] += 1
    # 正規化する
    total = sum(cnt)
    freq = list(map(lambda n: n / total, cnt))
    return (freq, lang)

# 各ファイルを処理する
def load_files(path):
    freqs =[]
    labels = []
    file_list = glob.glob(path)
    for fname in file_list:
        r = check_freq(fname)
        freqs.append(r[0])
        labels.append(r[1])
    return {"freqs":freqs, "labels":labels}

data = load_files("./lang/train/*.txt")
test = load_files("./lang/test/*.txt")
# 今後のためにJSONで結果を保存
with open("./lang/freq.json", "w", encoding="utf-8") as fp:
    json.dump([data, test], fp)

# 学習
clf = svm.SVC()
clf.fit(data["freqs"], data["labels"])

# 予測
predict = clf.predict(test["freqs"])

# 結果がどの程度あっていたか確認
ac_score = metrics.accuracy_score(test["labels"], predict)
cl_report = metrics.classification_report(test["labels"], predict)
print("正解率=", ac_score)
print("レポート=")
print(cl_report)
