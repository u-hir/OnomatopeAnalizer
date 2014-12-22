# coding: UTF-8
#スニペットのテキストを読んでオノマトペを含む一文を取り出すプログラム
#引数にスニペットのファイルを指定
import CaboCha
import sys
import os
import re
import MeCab

c = CaboCha.Parser()
m = MeCab.Tagger("-Ochasen")

#ファイルネームからオノマトペを取り出しておく
filename = sys.argv[1]
onomatopoeia = re.split('\/|\.', filename)[1]

#txtを開き一行(1スニペットづつ読む)


def main():
    if (len(sys.argv)<=2):
        print("1番目の引数にファイル名、\n2番目の引数に置換したい文字列を指定してください。")
        sys.exit()
    file_name = str(sys.argv[1]) # 1番目のコマンドライン引数
    word = str(sys.argv[2]) # 2番目のコマンドライン引数
    for snippet in open(file_name, "r"):
        sentences = split_snippet(snippet)
        sentence = extract_sentence(word, sentences)
        replaced_sentence = replace_word(word, sentence)
        print(replaced_sentence)

 
#スニペットを一文ずつに切り分けしてリストで返す
def split_snippet(snippet):
    sentences = re.split("。|\?|？|!|！|･|⁈|「|」|\s", snippet)
    return sentences


#指定した文字列を含むリストの要素を抽出し、リストで返す
def extract_sentence(word, sentences):
    for sentence in sentences:
        if word in sentence:
            print sentence
            return str(sentence)

    return ""


#指定文字を四角記号に置き換えして返す
def replace_word(word, sentence):
    word_len = len(word.decode('utf-8'))
    squares = "□" * word_len
    if word in sentence:
        replaced_sentence = sentence.replace(word, squares)
        return str(replaced_sentence)
    else:
        return ""


if (__name__ == '__main__'):
    main()
