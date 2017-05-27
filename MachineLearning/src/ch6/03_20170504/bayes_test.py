from bayes import BayesianFilter

bf = BayesianFilter()
# テキストを学習
bf.fit("激安セール - 今日だけ三割引", "広告")
bf.fit("クーポンプレゼント＆送料無料", "広告")
bf.fit("店内改装セール実施中", "広告")
bf.fit("美味しくなって再登場", "広告")
bf.fit("本日の予定の確認です", "重要")
bf.fit("プロジェクトの進捗確認お願いします", "重要")
bf.fit("打ち合わせよろしくお願いいたします", "重要")
bf.fit("会議の議事録です", "重要")
# 予測
pre, scorelist = bf.predict("激安、在庫一掃セール、送料無料")

print("結果=", pre)
print(scorelist)
