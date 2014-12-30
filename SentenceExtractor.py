# coding: utf-8
import sys
import re
import glob
def main():
    #if (len(sys.argv)<=2):
    #    print("1番目の引数にファイル名、\n2番目の引数に置換したい文字列を指定してください。")
    #    sys.exit()
    # file_name = str(sys.argv[1]) # 1番目のコマンドライン引数
    # word = str(sys.argv[2]) # 2番目のコマンドライン引数
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
    for sentence in sentences:
        if word in sentence:
            #print sentence
            return str(sentence)+'\n'

    return ""

if (__name__ == '__main__'):
    main()
