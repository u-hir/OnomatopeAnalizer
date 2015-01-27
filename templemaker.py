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
#    sentence_paths = ["sentences/ざあざあ.txt","sentences/しとしと.txt"]
#    sentence_paths = ["ざあざあ.txt","しとしと.txt"]
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
    rearact = {}
    act_freq_dic = {}

    for line in lines:
        linesplited = line.split(filename) #オノマトペで分離、前後文をリストに
        # オノマトペの前にある助詞「が」の前の名詞判定
        front = m.parseToNode(linesplited[0]) #オノマトペより前の文をめかぶに食わせて格納
        preterm = str() #手前文の単語を順番に
        frontterm = str() #直前の「が」の前確定

        while front:
            frontfeatures = front.feature.split(',')
            if frontfeatures[0] == "助詞":
                if frontfeatures[6] == "が" or frontfeatures[6] == "を" or frontfeatures[6] == "に" :
                    frontterm = preterm
            preterm = frontfeatures[6]
            front = front.next

        # オノマトペの直後にある動詞
        if len(linesplited) == 1:
            break
        rear = m.parseToNode(linesplited[1])
        if frontterm == str():
            pass
        else:
            while rear:
                rearfeatures = rear.feature.split(',')
                if rearfeatures[0] == "動詞":
#                    print frontterm.decode('utf-8') + "," + rearfeatures[6].decode('utf-8') + "," + line.decode("utf-8")
                    frontnouns.append(frontterm.decode('utf-8') + "/" + rearfeatures[6].decode('utf-8'))
                    break
                else:
                    rear = rear.next

    #単語組み合わせの回数カウント
    counter = Counter(frontnouns)
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

def normalize_unicode_nfc(word):
    word_unicode_nfd = word.decode('utf-8') # strからunicode(NFD)に変換
    word_unicode_nfc = unicodedata.normalize("NFC", word_unicode_nfd) # unicode(NFD)からunicode(NFC)に変換
    word_utf8 = word_unicode_nfc.encode('utf-8') # unicode to utf-8(str)
    return word_utf8



#メイン。指定されたファイルをdef mainにかけて、結果をprintする。
#この結果をリダイレクトしてcsvを生成していた。
if __name__ == '__main__':
    main()


