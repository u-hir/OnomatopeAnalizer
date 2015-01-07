-Onomatope Analizer-

オノマトペを含むスニペットをアメブロから収集するプログラム。
収集整理後、OnoSearch.pyにてオノマトペと関連語のスニペット内共起頻度を閲覧できる。





-Onomatope Analizerの使い方-

1. /onolist/以下に収集するオノマトペのリストを作成しおいておく。この時のファイル名が収集sunippetsファイルをrootに生成されるフォルダ名になる。

2.rootに生成されたスニペットテキストを含むフォルダを/snippets/以下に移動する。

3.SentenceExtractor.pyを実行し、/snippets/スニペットテキストからオノマトペを含む文章のみを抽出、/sentences/以下に保存。

4.rootのStopwords.txt内にストップワードにしたい語句を書いておく。

5.TFExporter.pyを実行し、/outputs/以下のファイルに含まれるオノマトペと共起単語の頻度を算出する。出力ファイルはcsv形式で/outputs/以下に保存。

6.OnoSearch.py実行時のコマンドライン引数に検索したい語句を１語つけて実行。該当するオノマトペと共起頻度が表示される。