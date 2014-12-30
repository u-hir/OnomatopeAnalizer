# -*- coding: utf-8 -*-
  
import MeCab                    # 形態素解析器MeCab
  
import math
 
# 文書集合のサンプル 
text = ["ミニアルバム☆ 新谷良子withPBB「BANDScore」 絶賛発売chu♪ いつもと違い、「新谷良子withPBB」名義でのリリース！！ 全５曲で全曲新録！とてもとても濃い１枚になりましたっ。 PBBメンバーと作り上げた、新たなバンビポップ。 今回も、こだわり抜いて", "2012年11月24日 – 2012年11月24日(土)／12:30に行われる、新谷良子が出演するイベント詳細情報です。", "単語記事: 新谷良子. 編集 Tweet. 概要; 人物像; 主な ... その『ミルフィーユ・桜葉』という役は新谷良子の名前を広く認知させ、本人にも大切なものとなっている。 このころは演技も歌も素人丸出し（ ... え、普通のことしか書いてないって？ 「普通って言うなぁ！」", "2009年10月20日 – 普通におっぱいが大きい新谷良子さん』 ... 新谷良子オフィシャルblog 「はぴすま☆だいありー♪」 Powered by Ameba ... 結婚 356 名前： ノイズh(神奈川県)[sage] 投稿日：2009/10/19(月) 22:04:20.17 ID:7/ms/OLl できたっちゃ結婚か", "2010年5月30日 – この用法の「壁ドン（壁にドン）」は声優の新谷良子の発言から広まったものであり、一般的には「壁際」＋「追い詰め」「押し付け」などと表現される場合が多い。 ドンッ. 「……黙れよ」. このように、命令口調で強引に迫られるのが女性のロマンの"] 
  
txt_num = len(text)
print 'total texts:', txt_num
print
  
fv_tf = []                      # ある文書中の単語の出現回数を格納するための配列
fv_df = {}                      # 単語の出現文書数を格納するためのディクショナリ
word_count = []                 # 単語の総出現回数を格納するための配列
  
fv_tf_idf = []                  # ある文書中の単語の特徴量を格納するための配列
  
count_flag = {}                 # fv_dfを計算する上で必要なフラグを格納するためのディクショナリ
  
# 各文書の形態素解析と、単語の出現回数の計算
for txt_id, txt in enumerate(text):
    # MeCabを使うための初期化
    tagger = MeCab.Tagger()
    node = tagger.parseToNode(txt.encode('utf-8'))
     
    fv = {}                     # 単語の出現回数を格納するためのディクショナリ
    words = 0                   # ある文書の単語の総出現回数
     
    for word in fv_df.keys():
        count_flag[word] = False
    while node.next:
        node = node.next
        surface = node.surface.decode('utf-8') # 形態素解析により得られた単語
  
        words += 1
  
        fv[surface] = fv.get(surface, 0) + 1 # fvにキー値がsurfaceの要素があれば、それに1を加え、なければ新しくキー値がsurfaceの要素をディクショナリに加え、値を1にする
  
        if surface in fv_df.keys(): # fv_dfにキー値がsurfaceの要素があれば
            if count_flag[surface] == False: # フラグを確認し，Falseであれば
                fv_df[surface] += 1 # 出現文書数を1増やす
                count_flag[surface] = True # フラグをTrueにする
        else:                 # fv_dfにキー値がsurfaceの要素がなければ
            fv_df[surface] = 1 # 新たにキー値がsurfaceの要素を作り，値として1を代入する
            count_flag[surface] = True # フラグをTrueにする
  
    fv_tf.append(fv)
    word_count.append(words)
  
# tf, idf, tf-idfなどの計算
for txt_id, fv in enumerate(fv_tf):
    tf = {}
    idf = {}
    tf_idf = {}
    for key in fv.keys():
        tf[key] = float(fv[key]) / word_count[txt_id] # tfの計算
        idf[key] = math.log(float(txt_num) / fv_df[key]) # idfの計算
        tf_idf[key] = (tf[key] * idf[key], tf[key], idf[key], fv[key], fv_df[key]) # tf-idfその他の計算
    tf_idf = sorted(tf_idf.items(), key=lambda x:x[1][0], reverse=True) # 得られたディクショナリtf-idfを、tf[key]*idf[key](tf-idf値)で降順ソート(処理後にはtf-idfはリストオブジェクトになっている)
    fv_tf_idf.append(tf_idf)
  
# 出力
for txt_id, fv in enumerate(fv_tf_idf):
    print 'This is the tf-idf of text', txt_id
    print 'total words:', word_count[txt_id]
    print
  
    for word, tf_idf in fv:
        print '%s\ttf-idf:%lf\ttf:%lf\tidf:%lf\tterm_count:%d\tdocument_count:%d' % (word, tf_idf[0], tf_idf[1], tf_idf[2], tf_idf[3], tf_idf[4]) # 左から順に、単語、tf-idf値、tf値、idf値、その文書中の単語の出現回数、その単語の出現文書数(これは単語ごとに同じ値をとる)
    print
