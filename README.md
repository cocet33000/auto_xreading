Auto Xreading
====

Xreadingをgoogle chromeで自動実行します。

## Requirement
- python3
  - selenium
- chromedriver

## 準備
- auto直下にSeleniumフォルダを作成
- 使用するOSとchromeのverとあったchromedriverをダウンロードして1.で作成したフォルダに入れる
  - (https://chromedriver.chromium.org/downloads)
- python3環境にseleniumライブラリをいれる
  -  `pip install selenium`
- 環境変数にxreading_usernameとxreading_passwordを追加する(bashrcなどに適当に以下を書き込む)
  -  `export xreading_username="your_username"`
  -  `export xreading_password="your_password"`

## 実行
- chromeでXreadingを開き、任意の本を読み始め、URLをコピー
- `python reading.py` を実行し、word数、読む速さ(words/min)、URLを入力
