### What I make
* iOSデバイスのスマホアプリでレシートの写真を撮影
* レシートの内容を家計簿管理
* **複数デバイス間（想定は家族内）で、家計簿管理を統合できるようにする（reppiを作りたい一番の目的）**

### How to use（現段階）
* `./reppi` に移動
* `python3.6 main.py -i [レシート画像ファイルの絶対パス] -k [Google Cloud API token]`
* ターミナルに `品名(str)と金額(int)のペア一覧(dict)` が表示される
* `python3.6 main.py -h(--help)` でヘルプ

### TODO
#### 機能面
- [x] ベースプログラム作成（コマンドライン引数に `レシート画像ファイルの絶対パス` と `Google Cloud API token` を渡すと、 `品名(str)と金額(int)のペア一覧(dict)` が返ってくるもの）
<<<<<<< HEAD
- [ ] 上記のRestAPI化（~~Django REST Framework使用予定~~ Falconで良さそう、バイナリーデータが送られてくることを前提で処理自体はベースと同じ）
- [ ] `品名(str)と金額(int)のペア一覧(dect)` をMySQLに保存
- [ ] SwiftでiOSアプリ実装（カメラでとった写真をバイナリーデータに変換し、reppiAPIに投げる）
#### その他
- [ ] ~~reppiAPI動作確認用のスクリプト作成（iOSアプリから投げられるリクエストと同じ形式でPOSTできるもの）~~ curlで代用
- [ ] reppiAPIをAWSにデプロイし、結果がAmazon RDSに保存されるようにする

### 参考資料
* [Google Cloud Vision API ~ Python を使用してリクエストを送信](https://cloud.google.com/vision/docs/using-python?hl=ja)
* [Cloud Vision APIの使い方まとめ](https://syncer.jp/cloud-vision-api)
* [[Python入門】argparseでコマンドライン引数を扱う方法](https://www.sejuku.net/blog/23647)
* [参考予定] [Django REST Frameworkを使って爆速でAPIを実装する](https://qiita.com/kimihiro_n/items/86e0a9e619720e57ecd8)
* [参考予定] [【Python】MySQLのデータベース操作](https://algorithm.joho.info/programming/python/sample-code-mysql-py/)
* [参考予定] [(下準備編)世界一丁寧なAWS解説。EC2を利用して、RailsアプリをAWSにあげるまで](https://qiita.com/naoki_mochizuki/items/f795fe3e661a3349a7ce)
* [参考予定] [curlのオプション--data, --data-binary, --data-raw, --data-urlencodeの違い](https://qiita.com/aosho235/items/d89bb027db0c5662d8c5)
* [参考予定] [Pythonで画像処理のWebAPIを作る ～Falcon編～](http://blog.apitore.com/2017/09/27/python-webapi-falcon/)
* [参考予定] [Python軽量フレームワークFalconでAPI開発 入門](https://qiita.com/shimakaze_soft/items/166071b17dd286e8913b)
=======
### 参考資料
* Cloud Vision API サンプルコード
https://cloud.google.com/vision/docs/using-python?hl=ja
* Cloud Vision API使い方
https://syncer.jp/cloud-vision-api
=======
- [ ] 上記のRestAPI化（Django REST Framework使用予定、バイナリーデータが送られてくることを前提で処理自体はベースと同じ）
- [ ] `品名(str)と金額(int)のペア一覧(dect)` をMySQLに保存
- [ ] SwiftでiOSアプリ実装（カメラでとった写真をバイナリーデータに変換し、reppiAPIに投げる）
#### その他
- [ ] reppiAPI動作確認用のスクリプト作成（iOSアプリから投げられるリクエストと同じ形式でPOSTできるもの）
- [ ] reppiAPIをAWSにデプロイし、結果がAmazon RDSに保存されるようにする

### 参考資料
* [Google Cloud Vision API ~ Python を使用してリクエストを送信](https://cloud.google.com/vision/docs/using-python?hl=ja)
* [Cloud Vision APIの使い方まとめ](https://syncer.jp/cloud-vision-api)
* [参考予定] [Django REST Frameworkを使って爆速でAPIを実装する](https://qiita.com/kimihiro_n/items/86e0a9e619720e57ecd8)
* [参考予定] [【Python】MySQLのデータベース操作](https://algorithm.joho.info/programming/python/sample-code-mysql-py/)
* [参考予定] [(下準備編)世界一丁寧なAWS解説。EC2を利用して、RailsアプリをAWSにあげるまで](https://qiita.com/naoki_mochizuki/items/f795fe3e661a3349a7ce)
>>>>>>> a587bdc... ベースは一旦完成
