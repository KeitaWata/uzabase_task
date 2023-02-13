# RSSフィードを取り込み、変換処理を行い、出力するアプリケーション

## 実行方法
### Requirement
- python3.9

## ローカル環境のセットアップ

### 1. インストール    
`$ pip install -r requirements.txt `  
※ 上記でインストールできなかった場合は、pip3で試してみる

### 2. フォルダーに移動して実行  
`$ python index.py `  
※ 上記でインストールできなかった場合は、python3で試してみる

## ファイルの説明

##  index.py
- 今回のアプリケーションの核となるPythonのファイル
- コメントアウトしている部分は、今回の課題の拡張機能となっているため、コメントアウトしてある状態にある

- 今回入力する値は、「<https://tech.uzabase.com/rss>」がベースとなっており、入力された値に「rss」という文字列が含まれているかを確認すると同時に、入力された値(URL)で開けることを確認した上で処理を行うように設計。
- 特定の文字(今回はNewsPicks)をreplaceを用いて削除している。

- 今回の課題の仕様変更、追加に対応できるようにstart関数でそれぞれの関数を呼び出す仕組みとしている。

- 簡単に、入力するrssの値を複数にするagain関数と出力したものをテキストファイルにするmktxt関数も作成した。それぞれ「#複数個rssを入力する際にコメントアウトを外す」と「#テキストファイル作成時にコメントアウトを外す」を実行すると指定のあった仕様変更・追加に準じている機能を使用することが可能。

- また、細かくに標準出力にエラー内容を表示するシステムにもなっている。

- mktxtで名前作ったテキストファイルはuploadsフォルダーに格納される。


##  requirements.txt
- 本アプリケーションを使用するにあたって、必要なライブラリーを一括でダウンロードできるテキストファイル


##  README.md
- 作成したアプリケーションの詳細と実行方法を記入