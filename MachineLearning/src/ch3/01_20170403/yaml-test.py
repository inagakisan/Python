import yaml

# YAMLの定義
yaml_str = """
Date: 2017-03-10
PriceList:
    -
        item_id: 1000
        name: Banana
        color: yellow
        price: 800
    -
        item_id: 1001
        name: Orange
        color: orange
        price: 1400
    -
        item_id: 1002
        name: Apple
        color: red
        price: 2400
"""

# YAMLを解析する
data = yaml.load(yaml_str)

# 名前と値段だけを表示する
for item in data['PriceList']:
    print(item["name"], item["price"])
