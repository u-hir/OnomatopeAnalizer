# coding: utf-8
import SnippetGetter as Snip
import os
import sys
import re
import MeCab

def split_snippet(snippet):
  sentences = re.split("。|\?|？|!|！|･|⁈|「|」|\s", snippet)
  return sentences

def extract_sentence(word, sentences):
  for sentence in sentences:
    if word in sentence:
      return str(sentence)

  return ""

def replace_word(word, sentence):
  word_len = len(word.decode('utf-8'))
  squares = "□" * word_len
  if word in sentence:
    replaced_sentence = sentence.replace(word, squares)
    return str(replaced_sentence)
  else:
    return ""

#snippets = Snip.get_ameba_single("ざあざあ")
#for snippet in snippets:
#  print(snippet)

if (__name__ == '__main__'):
  if (len(sys.argv)!=3):
    print("1番目の引数にファイル名、\n2番目の引数に置換したい文字列を指定してください。")
    sys.exit()
  file_name = str(sys.argv[1]) # 1番目のコマンドライン引数
  word = str(sys.argv[2]) # 2番目のコマンドライン引数
  for snippet in open(file_name, "r"):
    sentences = split_snippet(snippet)
    sentence = extract_sentence(word, sentences)
    replaced_sentence = replace_word(word, sentence)
    print(replaced_sentence)
