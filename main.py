# coding: utf-8
import SnippetGetter as Snip
import os
import sys
import re
import MeCab
from time import sleep


#onoclasslist = ["samui,tumetai", "suiteki,sitataru,otiru,haneru", "nagareru,tareru,sosogu", "simeru,nijimu", "nureru"]

onoclasslist = ["awateru,mogaku,otitukanai", "genkiganai", "genkina", "haku,modosu", "hatarakanai", "heiki,heizen", "hurueru", "hutotta,gankenna", "itamu", "iu,hanasu", "miru,mieru,niramu", "naku", "nemuru,neru", "nomu,you", "odoroku", "okiru,tatu", "okoru,hukigen,buaisou", "omou,kanjiru", "sawagu", "sekiwosuru,museru", "taberu,kamu,nameru", "tamerau,hirumu", "tukareru", "warau", "yaseta", "yorokobu"]


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
