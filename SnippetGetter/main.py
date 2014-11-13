# coding: utf-8
import SnippetGetter as Snip
import os
from time import sleep

##gitはじめたった

onomatopoeias = ["ほいほい"]
#onomatopoeias = ["うろうろ", "えっちらおっちら", "かっぽかっぽ", "さっさ", "さっさっ", "しゃなりしゃなり", "しゃらりしゃらり", "すたこら", "すたこらさっさ","すたすた", "せかせか", "たー", "たたーっ", "たかたか", "たじたじ", "だだーっ", "たたたた", "だだだだ", "たったかたったか", "たったっ", "たどたど", "ちょこちょこ", "てくてく", "てけてけ", "どっしどっし", "とーん", "とことこ", "とっとことっとこ", "とっと", "とっとっ", "ととと", "どたばた", "とぼとぼ", "のさのさ", "のしのし", "のそのそ", "のっしのっし", "のらりのらり", "のろのろ", "のろりのろり", "ぱかぱか", "ぱっぱか", "ぱたぱた", "ばたばた", "ぴたぴた", "ひょこひょこ", "ふらふら", "ぶらぶら", "よたよた", "よちよち", "よぼよぼ", "よろよろ", "らったった", "わたわた", "のこのこ", "ぱっぱ"]
#onomatopoeias = ["びゅうびゅう", "ざあざあ", "てくてく", "がたがた"]
for onomatope in onomatopoeias:
  snippets = Snip.get_ameba(onomatope)
  #スニペットを一行ずつ書き出し
  for snippet in snippets:
    txt = open('walkrun/'+onomatope+'.txt', 'a')
    txt.write(str(snippet)+'\n')
    txt.close()

  print onomatope
  print 'stop'
 #sleep(600)
  print 'restart'
