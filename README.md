# weather-app

1.実行方法：
# リポジトリをクローン
git clone https://github.com/TorryLiu/weather-app.git
cd weather-app

# アプリを実行
python main.py

アプリ起動後、コマンドライン上で以下の操作ができます：
都市名を入力して天気情報を取得
天気取得後にメモを登録
保存済みメモの参照（任意で一覧表示・削除も可能）

2.必要なライブラリ
本アプリでは外部ライブラリとしてrequestsを使用しています。  
以下のコマンドで必要なライブラリを一括インストールできます。
```bash
pip install -r requirements.txt

3.使用したAPIの説明
このアプリでは、WeatherAPI（https://www.weatherapi.com/） を利用して、指定した都市の現在の天気情報を取得しています。WeatherAPI は無料プランでも利用でき、都市名・緯度経度などから天気データを取得できるシンプルな REST API です。

エンドポイント：https://api.weatherapi.com/v1/current.json

パラメータ：
key: WeatherAPIのAPI キー
q: 都市名

レスポンス例：
{
  "location": {
    "name": "Tokyo"
  },
  "current": {
    "temp_c": 18.5,
    "condition": {
      "text": "Partly cloudy"
    }
  }
}
