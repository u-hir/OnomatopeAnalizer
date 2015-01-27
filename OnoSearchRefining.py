# coding: utf-8
import sys, codecs
import re
import glob
sys.stdout = codecs.EncodedFile(sys.stdout, 'utf_8')

result_dic = {}
result_dic2 = {}

def main():
    # outputファイルのパスを取得
    outputs_paths = glob.glob('output/*.csv')

    # パスからファイル名を取得
    outputs_file_names = [] # オノマトペのリスト
    for outputs_path in outputs_paths:
        outputs_path_splits = outputs_path.split("/") # パスの文字列を/で区切る
        outputs_txt_name = outputs_path_splits[-1] # 最後の要素が*.csv形式のファイル名
        outputs_txt_name_splits = outputs_txt_name.split(".")
        outputs_file_name = outputs_txt_name_splits[0] # オノマトペ
        outputs_file_names.append(outputs_file_name)

    for i, outputs_path in enumerate(outputs_paths):
        outputs_file_name = outputs_file_names[i] 
        for outputs_line in open(outputs_path, 'r'):
            freqdic = split_snippet(outputs_line, outputs_file_name) #共起頻度を取り出し

#文字列の一致を見る
def split_snippet(snippet, outputs_file_name):
    sentences = re.split(",", snippet)
    if sys.argv[1] in sentences[0]:
        result_dic.setdefault(str(outputs_file_name), sentences[1])

#メイン(二語目)
def main2(No1list):
    # 1語目のファイルを取得
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

    for outputs_path in No1list:
        outputs_file_name = "output/" + outputs_path + ".csv"   # outputs_file_names[i]
        fileonomatope = re.split('/|\.', outputs_file_name)[-2]
        for outputs_line in open(outputs_file_name, 'r'):
            split_snippet2(outputs_line, fileonomatope) #共起頻度を取り出し


#文字列の一致を見る(二語目)
def split_snippet2(snippet, outputs_file_name):
    sentences = re.split(",", snippet)
    if sys.argv[2] in sentences[0]:
        result_dic2.setdefault(str(outputs_file_name), sentences[1])
        

#指定した文字列を含むリストの要素を抽出し、リストで返す
def extract_sentence(word, sentences):
    for sentence in sentences:
        if word in sentence:
            return str(sentence)+'\n'

    return ""

if (__name__ == '__main__'):
    main()
    No1filename = [] # 1語目の該当ファイル名リスト
    No1freq = {}
    No2freq = {}
    Result = {}
    print "---------------" + sys.argv[1]  + "---------------"        
    for k, v in sorted(result_dic.items(),key=lambda x : float(x[1]),reverse=True):
        print k, v
        No1filename.append(k)
        No1freq[k] = v
    if len(sys.argv) == 3:
        print "---------------" + sys.argv[2]  + "---------------"
        main2(No1filename)
        for k2, v2 in sorted(result_dic2.items(),key=lambda x : float(x[1]),reverse=True):
            print k2, v2
            No2freq[k2] = v2
        print "---------------" + sys.argv[1] + " × "  + sys.argv[2]  + "---------------"
        for ono in No2freq:
            Result[ono] = float(No1freq[ono])*float(No2freq[ono])
        for kr, vr in sorted(Result.items(),key=lambda x : float(x[1]),reverse=True):
            print kr, vr
