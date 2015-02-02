# coding: utf-8
import MeCab
import glob
import unicodedata
import sys, codecs
from collections import Counter

sys.stdout = codecs.getwriter('utf-8')(sys.stdout)

def main():
    # 読み込むファイルのパスを取得
    sentence_paths = glob.glob('sentences/*.txt')
    for sentence_path in sentence_paths:
#        print "---------------------------------------"
        filename = get_filename(sentence_path)
        filename = normalize_unicode_nfc(filename)
        sentence_file = open(sentence_path, 'r')
        lines = sentence_file.readlines()
        word_dics = get_word_dics(lines, filename)
#        export_tf_csv(word_dics, filename)


def get_word_dics(lines, filename):
    #MeCabを使う
    m = MeCab.Tagger('-Ochasen -u userdic.dic')
    #前文名詞用リスト
    frontnouns = []
    combi_freq_dic = {}
    #後文動詞用dic
    rearacts = []
    act_freq_dic = {}

    line_nounact_combi = []

    for line in lines:
        linesplited = line.split(filename) #オノマトペで分離、前後文をリストに
        # オノマトペから始まる文の場合、名詞と動詞が挟んでいないので終了
        # オノマトペより前にある名詞
        front = m.parseToNode(linesplited[0]) #オノマトペより前の文をめかぶに食わせて格納
        preterm = [] #手前文の単語を前から順番に入れる変数
        while front:
            frontfeatures = front.feature.split(',')
            if frontfeatures[0] == "名詞":
                if frontfeatures[6] == "*":
                    pass
                else:
                    frontnouns.append(frontfeatures[6])
            front = front.next

        # オノマトペより後ろにある動詞
        rear = m.parseToNode(linesplited[1])
        while rear:
            rearfeatures = rear.feature.split(',')
            if rearfeatures[0] == "動詞":
                if rearfeatures[6] == "*":
                    pass
                else:
                    rearacts.append(rearfeatures[6])
            rear = rear.next

        for frontnoun in frontnouns:
            for rearact in rearacts:
                line_nounact_combi.append(frontnoun.decode('utf-8') + "/" + rearact.decode('utf-8'))
            

    #単語組み合わせの回数カウント
    counter = Counter(line_nounact_combi)
    for word, cnt in counter.most_common():
        combi_freq_dic.setdefault(word, cnt)
    combi_freq_list = combi_freq_dic.items()


    #出力
    write_path = "templates/"+filename+".csv"
    reset_file(write_path)
    write_file = open(write_path, 'a')
    for k, v in sorted(combi_freq_dic.items(),key=lambda x : x[1],reverse=True):
        write_line = k + "," + str(v)
        write_file.write(write_line.encode('utf-8')+'\n')
    print filename.decode('utf-8')

    # for k, v in nouns_count_dic.items():
    #     if int(v) != 1:
    #         nouns_freq_dic.setdefault(k, float(v)/len(lines))
    # for k, v in act_count_dic.items():
    #     if int(v) != 1:
    #         act_freq_dic.setdefault(k, float(v)/len(lines))

    # return nouns_freq_dic, act_freq_dic


def export_tf_csv(word_dics, filename):
    noun_dic = word_dics[0]
    act_dic = word_dics[1]

    write_path = "templates/"+filename+".csv"
    reset_file(write_path)
    write_file = open(write_path, 'a')
    for k, v in sorted(noun_dic.items(),key=lambda x : float(x[1]),reverse=True):
        write_line = k+","+str(v)+",名詞\n"
        write_file.write(write_line)

    for k, v in sorted(act_dic.items(),key=lambda x : float(x[1]),reverse=True):
        write_line = k+","+str(v)+",動詞\n"
        write_file.write(write_line)

def is_aster_or_filename(basic_type, filename):
    filename_normalize = normalize_unicode_nfc(filename)
    return basic_type == '*' or basic_type == filename_normalize

def get_filename(path):
    # パスからファイル名を取得
    path_splits = path.split("/") # パスの文字列を/で区切る
    txt_name = path_splits[-1] # 最後の要素が*.txt形式のファイル名
    txt_name_splits = txt_name.split(".")
    filename = txt_name_splits[0]
    return filename


# ファイルを初期化する
def reset_file(file_path):
    write_file = open(file_path, 'w')
    write_file.write('')

    # Macの濁音問題を直す
def normalize_unicode_nfc(word):
    word_unicode_nfd = word.decode('utf-8') # strからunicode(NFD)に変換
    word_unicode_nfc = unicodedata.normalize("NFC", word_unicode_nfd) # unicode(NFD)からunicode(NFC)に変換
    word_utf8 = word_unicode_nfc.encode('utf-8') # unicode to utf-8(str)
    return word_utf8


#メイン。指定されたファイルをdef mainにかけて、結果をprintする。
#この結果をリダイレクトしてcsvを生成していた。
if __name__ == '__main__':
    main()


