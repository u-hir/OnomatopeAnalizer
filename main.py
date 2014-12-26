# coding: utf-8
import SnippetGetter as Snip
import os
import sys
import re
import MeCab
from time import sleep

#weather = ["うらうら", "おっとり", "かっ", "かっか", "かんかん", "ぎらぎら", "けろり", "さんさん", "じりじり", "すかっ", "てかてか", "とっぷり", "なんなん", "ぽかぽか", "ぽっ", "ごろごろ", "こんこん", "ざーざー", "さーっ", "さっ", "ざーっ", "ざっ", "ざざっ", "ざんざら", "ざんざん", "しとしと", "じとじと", "じめじめ", "しゃりしゃり", "しょぼしょぼ", "ちらほら", "どしゃどしゃ", "どんより", "はらはら", "ばらばら", "ぱらぱら", "びしゃびしゃ", "びちゃびちゃ", "びしょびしょ", "びちょびちょ", "ぽつぽつ", "みりり", "ごーっ", "さーさー", "さーっ", "ざーっ", "さやさや", "さわさわ", "ざんざ", "すーすー", "すーっ", "すかすか", "そよそよ", "そよ", "そより", "はたはた", "ばたばた", "ぱたぱた", "ひゅー", "ぴゅー", "びゅー", "ひゅーひゅー", "びゅーびゅー", "ぴゅーぴゅー", "ひゅっ", "びゅっ", "ぴゅっ", "ひゅるるん", "びゅんびゅん", "ぴゅんぴゅん", "ふー", "ぶぉーっ", "ぶんぶん", "わさわさ"]

#walkrun = ["うろうろ", "えっちらおっちら", "かっぽかっぽ", "さっさ", "さっさっ", "しゃなりしゃなり", "しゃらりしゃらり", "すたこら", "すたこらさっさ","すたすた", "せかせか", "たー", "たたーっ", "たかたか", "たじたじ", "だだーっ", "たたたた", "だだだだ", "たったかたったか", "たったっ", "たどたど", "ちょこちょこ", "てくてく", "てけてけ", "どっしどっし", "とーん", "とことこ", "とっとことっとこ", "とっと", "とっとっ", "ととと", "どたばた", "とぼとぼ", "のさのさ", "のしのし", "のそのそ", "のっしのっし", "のらりのらり", "のろのろ", "のろりのろり", "ぱかぱか", "ぱっぱか", "ぱたぱた", "ばたばた", "ぴたぴた", "ひょこひょこ", "ふらふら", "ぶらぶら", "よたよた", "よちよち", "よぼよぼ", "よろよろ", "らったった", "わたわた", "のこのこ", "ぱっぱ"]
#onomatopoeias = ["びゅうびゅう", "ざあざあ", "てくてく", "がたがた"]


onoclasslist = ["samui,tumetai", "suiteki,sitataru,otiru,haneru", "nagareru,tareru,sosogu", "simeru,nijimu", "nureru"]

def main(onomatope):
#  for onomatope in onomatopoeias:
    snippets = Snip.get_ameba(onomatope)
    for snippet in snippets:
        txt = open(onoclass+'/'+str(onomatope)+'.txt', 'a')
        txt.write(str(snippet)+'\n')
        txt.close()

    print onoclass + '/' + onomatope + '.txt'
    print onomatope
    print 'stop'
    sleep(300)
    print 'restart'

    
if (__name__ == '__main__'):
    for onoclass in onoclasslist:
        file = open("onolist/"+onoclass+".txt", 'r')
        text = file.readlines()
        os.mkdir(onoclass)
        for onomatope in text:
            print onomatope
            main(onomatope.rstrip())
