# coding: utf-8
import MeCab
import glob
import unicodedata
import sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout)

def main():
    # 読み込むファイルのパスを取得
#    sentence_paths = glob.glob('sentences/*.txt')
    sentence_paths = ["ざあざあ.txt","しとしと.txt"]
    for sentence_path in sentence_paths:
        filename = get_filename(sentence_path)
        sentence_file = open(sentence_path, 'r')
        lines = sentence_file.readlines()
        word_dics = get_word_dics(lines, filename)
#        export_tf_csv(word_dics, filename)


def get_word_dics(lines, filename):
    #MeCabを使う
    m = MeCab.Tagger('-Ochasen -u userdic.dic')
    #名詞格納用dic
    nouns_count_dic = {}
    nouns_freq_dic = {}
    #動詞格納用dic
    act_count_dic = {}
    act_freq_dic = {}
    for line in lines:
        linesplited = line.split(filename) #オノマトペで分離、前後文をリストに
        print filename.decode('utf-8')
        for feature in linesplited:
            print feature.decode('utf-8')
        front = m.parseToNode(linesplited[0]) #オノマトペより前の文をめかぶに食わせて格納
        preterm = []
        while front:
            frontfeatures = front.feature.split(',')
            if frontfeatures[0] == "助詞":
                if frontfeatures[6] == "が":
                    rear = m.parseToNode(linesplited[1])
                    while rear:
                        rearfeatures = front.feature.split(',')
                        print rearfeatures[0].decode('utf-8')
                        if rearfeatures[0] == "動詞":
                            print preterm.decode('utf-8') + "," + rearfeatures[6].decode('utf-8')
                            print "ok"
                            break
                        else:
                            rear = rear.next
            else:
                preterm = frontfeatures[6]
            front = front.next
        print "------------------"
        

        node = m.parseToNode(line) #一行をめかぶに食わせる
        while node:
            #featureはMeCabにかけて取れた品詞名などのこと。「,」区切りになってる
            features = node.feature.split(',')

            # if features[6] == "*":
            #     for feature in features:
            #         print feature.decode("utf-8")

            #feature[0]は品詞が書かれている部分
            word_class = features[0]
            #feature[6]はその単語の基本形が書かれている
            basic_type = features[6]
            
            if is_aster_or_filename(basic_type, filename): # 基本形が*の場合は記号なので、飛ばす
                node = node.next
                continue

            if word_class == "名詞":
                nouns_count_dic.setdefault(basic_type, 0)
                nouns_count_dic[basic_type] += 1
            if word_class == "動詞":
                act_count_dic.setdefault(basic_type, 0)
                act_count_dic[basic_type] += 1
            node = node.next
    for k, v in nouns_count_dic.items():
        if int(v) != 1:
            nouns_freq_dic.setdefault(k, float(v)/len(lines))
    for k, v in act_count_dic.items():
        if int(v) != 1:
            act_freq_dic.setdefault(k, float(v)/len(lines))

    return nouns_freq_dic, act_freq_dic


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


