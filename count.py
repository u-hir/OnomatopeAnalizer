# -*- coding:utf-8 -*-
import MeCab
import sys

#1行1ツイートのテキストを読んで、名詞、動詞、形容詞に分解し、各単語の出現回数を数えるプログラム
#カウント後に表示される各単語は基本形に直している

def main(path):
    #MeCabを使う
    m = MeCab.Tagger('-Ochasen')
    #名詞格納用dic
    nouns = {}
    #動詞格納用dic
    act = {}
    #形容詞格納用dic
    adject = {}
    #副詞格納用dic
    adverb = {}

    #文書読み込み
    lines = open(path,"r").readlines()
    for line in lines:
        node = m.parseToNode(line)
        while node:
            #featureはMeCabにかけて取れた品詞名などのこと。「,」区切りになってる
            features = node.feature.split(',')
            #feature[0]は品詞が書かれている部分
            noun = features[0]
            #feature[6]はその単語の基本形が書かれている
            basic = features[6]
            if basic == '*': # 基本形が*の場合は記号なので、飛ばす
                continue
            #nounが名詞だった場合、名詞のカウンタを一つ回す
            if noun == "名詞":
                nouns.setdefault(basic, 0)
                nouns[basic] += 1
            if noun == "動詞":
                act.setdefault(basic, 0)
                act[basic] += 1
            if noun == "形容詞":
                adject.setdefault(basic, 0)
                adject[basic] += 1
            if noun == "副詞":
                adverb.setdefault(basic, 0)
                adverb[basic] += 1

            node = node.next

    return nouns, act, adject, adverb


#メイン。指定されたファイルをdef mainにかけて、結果をprintする。
#この結果をリダイレクトしてcsvを生成していた。
if __name__ == '__main__':
    dic = main(sys.argv[1])
    nounDic = dic[0]
    actDic = dic[1]
    adjectDic = dic[2]
    adverbDic = dic[3]

    for k, v in sorted(nounDic.items(),key=lambda x : int(x[1]),reverse=True):
        #if v >= 5:
            print "%s , %d, 名詞" %(k,v)


    for k, v in sorted(actDic.items(),key=lambda x : int(x[1]),reverse=True):
        #if v >= 5:
            print "%s , %d , 動詞" %(k,v)


    for k, v in sorted(adjectDic.items(),key=lambda x : int(x[1]),reverse=True):
        #if v >= 5:
            print "%s , %d , 形容詞" %(k,v)

    for k, v in sorted(adverbDic.items(),key=lambda x : int(x[1]),reverse=True):
        #if v >= 5:
            print "%s , %d , 副詞" %(k,v)
