import json
from datetime import datetime
# from モジュール import クラス
import logging

def get_today_filename():
    today = datetime.now().strftime("%Y%m%d")
    # モジュール全体読み込む場合：datetime.datetime.now()
    # datetime.now()の場合:2026-04-01 10:18:23.123456
    # string + format + time　日付⇒文字列
    # string + parse + time 文字列⇒日付
    return f"{today}.json"
    # "20260401.json"
    # 後でこの形で使う：filename = get_today_filename()

def save_memo(city, data):
    filename = get_today_filename()
    #ファイル名指定済み

    memo = { #辞書dict　キー：値
        "都市名": city,
        "天気概要": data["current"]["condition"]["text"],
        #JSON階層関係ある
        "気温": data["current"]["temp_c"],
        #JSON階層関係ある
        "辞書作成練習": "辞書作成テスト"
        #{"都市名": "London", "天気概要": "Partly cloudy", "気温": 8.3, "辞書作成練習": "辞書作成テスト"}
    }
    # city dataどこで定義されたの？ cityはmain.pyで提供　dataはweather_api.py⇒main.pyで提供

    with open(filename, "a", encoding="utf-8") as f:
        #ファイルがなければ新しく作る
        # w　上書き
        #ファイルの文字コードを決める
        json.dump(memo, f, ensure_ascii=False)
        #漢字表示：ensure_ascii=False Unicodeに変換しないで、日本語そのまま表示してっていう命令を出す
        f.write("\n")
    #with..as..は構文syntax;ほか：if for
    #open()は関数function
    # open()の返り値をfに付与、fはほかの名前にされても可能
    logging.info(f"保存完了: {city} → {filename}")
    #　下記のように、括弧中での内容は自分指定可能
    # logging.info("天気データを保存しました")
    # logging.error("API からデータを取得できませんでした")
    # logging.warning("入力された都市名が空です")


def list_memos():
    filename = get_today_filename()
    print("■ メモ一覧表示")

    with open(filename, "r", encoding="utf-8") as f:
    # r read w a
        for i, line in enumerate(f, start=10):
        # enumerate()、内部関数、ループに番号付ける、枚举列举
        #for index, value in enumerate(['apple', 'banana', 'cherry']):
        #  print(index, value)
        # iとlineは他の名前指定か
        # 関数enumerate()のオプションstart=1
        # タプル：tuple　t = (10, 20)
            memo = json.loads(line)
            #json.loads():JSON⇒辞書
            print(f"{i}. {memo['都市名']} / {memo['天気概要']} / {memo['気温']}℃") 

def delete_memo():
    filename = get_today_filename()

    with open(filename, "r", encoding="utf-8") as f:
        memos = [json.loads(line) for line in f]

    for i, memo in enumerate(memos, start=1):
        print(f"{i}. {memo['都市名']} / {memo['天気概要']} / {memo['気温']}℃")

    num = int(input("削除したい番号を入力してください: "))

    if 1 <= num <= len(memos):
        del memos[num - 1]
        print("削除しました。")
    else:
        print("番号が不正です。")
        logging.error(f"存在しない番号: {num}")
        return

    with open(filename, "w", encoding="utf-8") as f:
        for memo in memos:
            json.dump(memo, f, ensure_ascii=False)
            f.write("\n")
