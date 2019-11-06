Auto Xreading
====

Xreading を google chrome で自動実行します。(たまに失敗します)

## Requirement
- python3
  - selenium
- chromedriver

## 準備
- auto_xreading 直下に Selenium フォルダを作成
- 以下のリンクから使用する OS と chrome の ver と合う chromedriver をダウンロードして1.で作成したフォルダに入れる
  - https://chromedriver.chromium.org/downloads
- python3環境に selenium ライブラリをいれる
  -  `pip install selenium`
- 環境変数に xreading_username と xreading_password を追加する( bashrc などに適当に以下を書き込む)
  -  `export xreading_username="your_username"`
  -  `export xreading_password="your_password"`

## 実行
- chrome で Xreading を開き、任意の本を読み始め、URLをコピー
- `python reading.py` を実行し、word数、読む速さ(words/min)、URLを入力
