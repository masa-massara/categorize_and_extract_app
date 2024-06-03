# extract_proper_noun_api

## 概要

このアプリケーションは、GoogleのGenerative AIを使用してテキストから固有名詞を抽出する機能を提供します。

## インストール方法

以下のコマンドを使用して、必要なパッケージをインストールします。

```bash
pip install -r requirements.txt
```

## 使い方

アプリケーションを起動するには、以下のコマンドを実行します。
```
python app/main.py
```

その後、以下のような形式でGETリクエストを送信します。
```
http://localhost:8000/extract?text=<抽出したいテキスト>
```
