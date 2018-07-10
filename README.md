### 準備
#### RDB
* ローカルのMySQLに `reppi` データベースを作成し、 `reppi/mysql/reppi.sql` でテーブルを作成する。
* `reppi/` に `reppi.dat` ファイルを作成し、下記を記載する。
```
[Mysql]
  Host:     [ローカルのホスト名]
  User:     [ローカルのユーザー名]
  Password: [ローカルのパスワード]
```
#### Google Cloud API
* Cloud Vision APIを使うために、アカウント作成からAPIkey発行までの下準備をする。
ref. https://syncer.jp/cloud-vision-api

### 実行
* ターミナルで `./reppi` で `python3.6 main.py -i [レシート画像ファイルの絶対パス] -k [Google Cloud API token]` を実行する。

### 結果
* `品名(str)と金額(int)のペア一覧(list)` がターミナルに表示される。
* 同内容ががMySQLに保存される。

### その他
* `python3.6 main.py -h` でヘルプが表示される。
