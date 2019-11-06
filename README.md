Auto Xreading
====

Xreadingをgoogle chromeで自動実行します。

## Requirement
- python3
  - selemium
- chromedriver

## 準備
1. auto直下にSeleniumフォルダを作成
2. 使用するOSとchromeのverとあったchromedriverをダウンロードし1.で作成したフォルダに入れる
  link(https://chromedriver.chromium.org/downloads)
3. python3環境にて　pip install selenium
4. 環境変数にxreading_usernameとxreading_passwordを追加

##実行
1. chromeでXreadingを開き、任意の本を読み始め、URLをコピー
2. python reading.py を実行し、word数、読む速さ(words/min)、URLを入力
