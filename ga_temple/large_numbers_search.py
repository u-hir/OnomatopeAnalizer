# coding: utf-8
import sys
import re
import glob
import shutil

result_dic = {}
values = []

def main():
    # templeファイルのパスを取得
    outputs_paths = glob.glob('*.csv')

    # パスからファイル名を取得
    outputs_file_names = []
    for outputs_path in outputs_paths:
#        outputs_path_splits = outputs_path.split("/") # パスの文字列を/で区切る
#        outputs_txt_name = outputs_path_splits[-1] # 最後の要素が*.csv形式のファイル名
#        outputs_txt_name_splits = outputs_txt_name.split(".")
        outputs_txt_name_splits = outputs_path.split(".")        
        outputs_file_name = outputs_txt_name_splits[0]
        outputs_file_names.append(outputs_file_name)

    for i, outputs_path in enumerate(outputs_paths):
        outputs_file_name = outputs_file_names[i]
        write_file_path = 'search/'+outputs_file_name+'.txt' # 書き込むファイルのパス
        for outputs_line in open(outputs_path, 'r'):
            r = look_templates(outputs_line, outputs_file_name)
            if r is None:
                pass
            else:
                values.append(r)
    text = open("large_numbers.txt", "w")
    for value in values:
        text.writelines(value)

    copy_large_numbers(values)
        

#最初の一行を読んで出現回数を参照
def look_templates(snippet, outputs_file_name):
    sentences = re.split(",", snippet)
    if int(sentences[1]) > 4:
        print outputs_file_name
        print sentences[1]
        countnumber = sentences[1]
        result_dic.setdefault(str(outputs_file_name), sentences[1])
        return outputs_file_name,str(countnumber)


#フォルダに該当ファイルをコピー
def copy_large_numbers(values):
    for value in values:
        print value
        filename = value[0]
        shutil.copy(filename+".csv", "large_numbers")


if (__name__ == '__main__'):
    main()

