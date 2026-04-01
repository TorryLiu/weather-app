import logging

def setup_logger():
    logging.basicConfig(
        filename="weather.log", 
        # 保存先
        level=logging.INFO,
        # レベル:DEBUG; INFO; WARNING; ERROR; CRITICAL
        format="%(asctime)s - %(levelname)s - %(message)s", 
        # 形式
        # 例：2026-04-01 09:45:55,184 - INFO - 保存完了: Anshan → 20260401.json
        # Pythonのフォーマット記法：%(文字列として入れる)s
        # ハイフンは区切り記号,文字まで指定ても可能（下記のようにテストした）
        # 2026-04-01 09:57:49,643 文字は ERROR - 存在しない番号: 5
        # 2026-04-01 09:57:50,410 文字は INFO - 操作終了
        # asctime levelname message:内部キーワード、変更不可
        encoding="utf-8"
        #漢字が文字化けしないように
    )
    #logging.basicConfig():Pythonのログ機能の初期設定関数(function,函数)

