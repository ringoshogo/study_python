
### 検索ツールサンプル
### これをベースに課題の内容を追記してください
import csv
import itertools

# 検索ソース
source=["ねずこ","たんじろう","きょうじゅろう","ぎゆう","げんや","かなお","ぜんいつ"]

### 検索ツール
def search():
    word =input("鬼滅の登場人物の名前を入力してください >>> ")
    
    ### ここに検索ロジックを書く

    # 課題3 csvファイルを読み込む
    source = __read_csv()

    # 課題1 sourceにおける存在有無をチェックする
    if __has_search_str(word, source):
        print("{}が見つかりした。".format(word))
    else:
        print("{}が見つかりませんでした。".format(word))
        
        # 課題2 sourceに存在しない場合は追加する
        source.append(word)

    # 課題4 csvファイルに書き込む
    __write_csv(source)

def __has_search_str(search_str: str, target_source: list) -> bool:
    """引数の文字列が検索ソースに存在するか否かを判定する"""
    
    for src_elm in target_source:
        if src_elm == search_str:
            return True

    return False

def __read_csv() -> list:
    """csvファイルを読み込んでlistを返却する"""

    with open("./csv/source.csv", "r", encoding="utf-8") as csv_file:
        return list(itertools.chain.from_iterable(csv.reader(csv_file)))

def __write_csv(target_source: list):
    """引数のリストをcsvファイルに書き込む"""

    with  open("./csv/source.csv", "w", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(target_source)
        csv_file.flush()

if __name__ == "__main__":
    search()
