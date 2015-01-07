# coding: utf-8
import sys
import re
import glob

result_dic = {}

def main():
    # outputファイルのパスを取得
    outputs_paths = glob.glob('output/*.csv')

    # パスからファイル名を取得
    outputs_file_names = []
    for outputs_path in outputs_paths:
        outputs_path_splits = outputs_path.split("/") # パスの文字列を/で区切る
        outputs_txt_name = outputs_path_splits[-1] # 最後の要素が*.csv形式のファイル名
        outputs_txt_name_splits = outputs_txt_name.split(".")
        outputs_file_name = outputs_txt_name_splits[0]
        outputs_file_names.append(outputs_file_name)

    for i, outputs_path in enumerate(outputs_paths):
        outputs_file_name = outputs_file_names[i]
        write_file_path = 'search/'+outputs_file_name+'.txt' # 書き込むファイルのパス
        for outputs_line in open(outputs_path, 'r'):
            freqdic = split_snippet(outputs_line, outputs_file_name) #共起頻度を取り出し

#文字列の一致を見る
def split_snippet(snippet, outputs_file_name):
    sentences = re.split(", ", snippet)    
    if sys.argv[1] == sentences[0]:
        result_dic.setdefault(str(outputs_file_name), sentences[1])

#指定した文字列を含むリストの要素を抽出し、リストで返す
def extract_sentence(word, sentences):
    for sentence in sentences:
        if word in sentence:
            return str(sentence)+'\n'

    return ""

if (__name__ == '__main__'):
    main()
    for k, v in sorted(result_dic.items(),key=lambda x : float(x[1]),reverse=True):
        print k, v
