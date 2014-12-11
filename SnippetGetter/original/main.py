# coding: utf-8
import SnippetGetter as Snip
import os

snippets = Snip.get_ameba(["雨", "ざあざあ"])
for snippet in snippets:
  print(snippet)
  for snippet in snippets:
    txt = open('onomatope.txt', 'a')
    txt.write(str(snippet)+'\n')
    txt.close()
