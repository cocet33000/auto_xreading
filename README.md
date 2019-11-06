Auto Xreading
====

Xreadingをgoogle chromeで自動実行します。

## Requirement
- python3
  - selemium
- chromedriver

## 準備
- auto直下にSeleniumフォルダを作成
- 使用するOSとchromeのverとあったchromedriverをダウンロードして1.で作成したフォルダに入れる
  - (https://chromedriver.chromium.org/downloads)
- python3環境にて　`pip install selenium`
- 環境変数にxreading_usernameとxreading_passwordを追加

## 実行
- chromeでXreadingを開き、任意の本を読み始め、URLをコピー
- `python reading.py` を実行し、word数、読む速さ(words/min)、URLを入力
