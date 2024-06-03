# extract_proper_noun_api

## 概要

このアプリケーションは、Googleのgeminiを使用してテキストから固有名詞を抽出するapiです。

## インストール方法

以下のコマンドを使用して、必要なパッケージをインストールします。

```bash
pip install -r requirements.txt
```

## 環境変数の設定
アプリケーションを動作させるために、以下の内容で .env ファイルをプロジェクトのルートディレクトリに作成してください。
```
GEMINI_API_KEY=<取得したAPIキー>
```
<取得したAPIキー>の部分を、APIキーに置き換えてください。
APIキーの作り方は[こちら](https://aistudio.google.com/app/tuned_models/new_tuned_model)を参照してください。


## 使い方

アプリケーションを起動するには、以下のコマンドを実行します。
```
python app/main.py
```

その後、以下のような形式でGETリクエストを送信します。
```
http://localhost:8000/extract?text=<抽出したいテキスト>
```

アプリケーションのテストを実行するには、以下のコマンドを実行します。
```
pytest
```
