# coding: UTF-8
import CaboCha
import sys
import os
import re
import MeCab
#txtを読んでオノマトペを含む一文を取り出し

c = CaboCha.Parser()
m = MeCab.Tagger("-Ochasen")

#ファイルネームからオノマトペを取り出しておく
filename = sys.argv[1]
onomatopoeia = re.split('\/|\.', filename)[1]

#txtを開き一行(1スニペットづつ読む)
txt = open(sys.argv[1])
snippets = txt.readlines()
for snippet in snippets:
    sentences = re.split('。| |、',str(snippet))
    for sentence in sentences:
        if onomatopoeia in sentence:
            print '------------------------------------------'
            print sentence
            print c.parseToString(sentence)
            print m.parse(sentence)
        #else:
            #print 'false'
