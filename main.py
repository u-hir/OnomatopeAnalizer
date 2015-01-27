# coding: utf-8
import SnippetGetter as Snip
import os
import sys
import re
import MeCab
from time import sleep


onoclasslist = ["susumu,hakobu","otiru","oreru","yureru","kiru,kireru","yaburu,yabureru","haru,kuttuku","sasu","magaru,siwagayoru"]

def main(onomatope):
#  for onomatope in onomatopoeias:
    snippets = Snip.get_ameba(onomatope)
    for snippet in snippets:
        txt = open(onoclass+'/'+str(onomatope)+'.txt', 'a')
        txt.write(str(snippet)+'\n')
        txt.close()

    print onoclass + '/' + onomatope + '.txt'
    print 'stop'
    sleep(600)
    print 'restart'

    
if (__name__ == '__main__'):
    for onoclass in onoclasslist:
        file = open("onolist/"+onoclass+".txt", 'r')
        text = file.readlines()
        os.mkdir(onoclass)
        for onomatope in text:
            print onomatope
            main(onomatope.rstrip())
