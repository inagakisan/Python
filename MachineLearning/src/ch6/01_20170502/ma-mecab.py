import MeCab
mecab = MeCab.Tagger("-Ochasen") # Mecabオブジェクトを生成
malist = mecab.parse("庭には二羽鶏がいる。") # 形態素解析を行う
print(malist)
