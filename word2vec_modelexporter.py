# coding: utf-8
import sys
import re
import glob
import unicodedata
def main():
    # スニペットファイルのパスを取得
    snip_paths = glob.glob('snippets/*/*/*.txt')

    # パスからファイル名を取得
    snip_file_names = []
    for snip_path in snip_paths:
        snip_path_splits = snip_path.split("/") # パスの文字列を/で区切る
        snip_txt_name = snip_path_splits[-1] # 最後の要素が*.txt形式のファイル名
        snip_txt_name_splits = snip_txt_name.split(".")
        snip_file_name = snip_txt_name_splits[0]
        snip_file_names.append(snip_file_name)

    for i, snip_path in enumerate(snip_paths):
        snip_file_name = snip_file_names[i]
        write_file_path = 'sentences/'+snip_file_name+'.txt' # 書き込むファイルのパス
        reset_file(write_file_path) # ファイルを初期化
        for snip_line in open(snip_path, 'r'):
            sentences = split_snippet(snip_line) # 文ごとに分割する
            sentence = extract_sentence(snip_file_name, sentences) # オノマトペを含む一文のみを返す
            write_file = open(write_file_path, 'a')
            write_file.write(sentence) # ファイルに書き込む

# ファイルを初期化する
def reset_file(file_path):
    file = open(file_path, 'w')
    file.write('')

#スニペットを一文ずつに切り分けしてリストで返す
def split_snippet(snippet):
    sentences = re.split("。|\?|？|!|！|･|⁈|「|」|\s", snippet)
    return sentences


#指定した文字列を含むリストの要素を抽出し、リストで返す
def extract_sentence(word, sentences):
    word_normalize = normalize_unicode_nfc(word)
    for sentence in sentences:
        if word_normalize in sentence:
            #print sentence
            return str(sentence)+'\n'

    return ""

# Macの濁音問題を直す
def normalize_unicode_nfc(word):
    word_unicode_nfd = word.decode('utf-8') # strからunicode(NFD)に変換
    word_unicode_nfc = unicodedata.normalize("NFC", word_unicode_nfd) # unicode(NFD)からunicode(NFC)に変換
    word_utf8 = word_unicode_nfc.encode('utf-8') # unicode to utf-8(str)
    return word_utf8

if (__name__ == '__main__'):
    main()
