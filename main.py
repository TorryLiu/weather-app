from logger_setup import setup_logger
from weather_api import fetch_weather
from memo_manager import save_memo, list_memos, delete_memo
import logging

setup_logger()

api_key = "ec40b738dc39488794835518263103"

def add_line():
    city = input("都市名を入力してください: ")
    logging.info(f"検索開始: {city}")

    data = fetch_weather(city, api_key)

    if "error" in data:
        print("エラー：存在しない都市名です。")
        logging.error(f"存在しない都市名: {city}")
        return

    save_memo(city, data)

while True:
    print("\n=== 天気メモアプリ ===")
    print("1. 天気を取得してメモを保存")
    print("2. メモ一覧表示")
    print("3. メモ削除")
    print("4. 終了")

    choice = input("番号を選んでください: ")

    if choice == "1":
        add_line()
    elif choice == "2":
        list_memos()
    elif choice == "3":
        delete_memo()
    elif choice == "4":
        print("ご使用ありがとうございます。また待ちしております。")
        logging.info("操作終了")
        break
    else:
        print("無効な入力です。")
        logging.error(f"存在しない番号: {choice}")
