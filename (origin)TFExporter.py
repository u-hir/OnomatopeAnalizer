# coding: utf-8
import MeCab
import glob
<<<<<<< HEAD
=======
import unicodedata
>>>>>>> a81e408aa4993ed353759e22942eda6079ee5213

def main():
    # 読み込むファイルのパスを取得
    sentence_paths = glob.glob('sentences/*.txt')
    sentence_paths = filter_file(sentence_paths) # 50行未満のファイルを削除
<<<<<<< HEAD
=======
    line_len_filename = "lines_len.csv"
    reset_file(line_len_filename)
>>>>>>> a81e408aa4993ed353759e22942eda6079ee5213
    for sentence_path in sentence_paths:
        filename = get_filename(sentence_path)
        sentence_file = open(sentence_path, 'r')
        lines = sentence_file.readlines()
<<<<<<< HEAD
=======
        export_line_len_csv(len(lines), filename, line_len_filename)
>>>>>>> a81e408aa4993ed353759e22942eda6079ee5213
        word_dics = get_word_dics(lines, filename)
        export_tf_csv(word_dics, filename)

def get_word_dics(lines, filename):
    #MeCabを使う
    m = MeCab.Tagger('-Ochasen -u userdic.dic')
    #名詞格納用dic
    nouns_count_dic = {}
    nouns_freq_dic = {}
    #動詞格納用dic
    act_count_dic = {}
    act_freq_dic = {}
    #形容詞格納用dic
    adject_count_dic = {}
    adject_freq_dic = {}
    #副詞格納用dic
    adverb_count_dic = {}
    adverb_freq_dic ={}


    for line in lines:
        node = m.parseToNode(line)
        while node:
            #featureはMeCabにかけて取れた品詞名などのこと。「,」区切りになってる
            features = node.feature.split(',')
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
            if word_class == "形容詞":
                adject_count_dic.setdefault(basic_type, 0)
                adject_count_dic[basic_type] += 1
            if word_class == "副詞":
                adverb_count_dic.setdefault(basic_type, 0)
                adverb_count_dic[basic_type] += 1
            node = node.next
    for k, v in nouns_count_dic.items():
        if int(v) != 1:
            nouns_freq_dic.setdefault(k, float(v)/len(lines))
    for k, v in act_count_dic.items():
        if int(v) != 1:
            act_freq_dic.setdefault(k, float(v)/len(lines))
    for k, v in adject_count_dic.items():
        if int(v) != 1:
            adject_freq_dic.setdefault(k, float(v)/len(lines))
    for k, v in adverb_count_dic.items():
        if int(v) != 1:
            adverb_freq_dic.setdefault(k, float(v)/len(lines))

    return nouns_freq_dic, act_freq_dic, adject_freq_dic, adverb_freq_dic

def export_tf_csv(word_dics, filename):
    noun_dic = word_dics[0]
    act_dic = word_dics[1]
    adject_dic = word_dics[2]
    adverb_dic = word_dics[3]
    write_path = "output/"+filename+".csv"
    reset_file(write_path)
    write_file = open(write_path, 'a')
    for k, v in sorted(noun_dic.items(),key=lambda x : float(x[1]),reverse=True):
        write_line = k+", "+str(v)+", 名詞\n"
        write_file.write(write_line)

    for k, v in sorted(act_dic.items(),key=lambda x : float(x[1]),reverse=True):
        write_line = k+", "+str(v)+", 動詞\n"
        write_file.write(write_line)

    for k, v in sorted(adject_dic.items(),key=lambda x : float(x[1]),reverse=True):
        write_line = k+", "+str(v)+", 形容詞\n"
        write_file.write(write_line)

    for k, v in sorted(adverb_dic.items(),key=lambda x : float(x[1]),reverse=True):
        write_line = k+", "+str(v)+", 副詞\n"
        write_file.write(write_line)

def is_aster_or_filename(basic_type, filename):
<<<<<<< HEAD
    return basic_type == '*' or basic_type == filename
=======
    filename_normalize = normalize_unicode_nfc(filename)
    return basic_type == '*' or basic_type == filename_normalize
>>>>>>> a81e408aa4993ed353759e22942eda6079ee5213

def get_filename(path):
    # パスからファイル名を取得
    path_splits = path.split("/") # パスの文字列を/で区切る
    txt_name = path_splits[-1] # 最後の要素が*.txt形式のファイル名
    txt_name_splits = txt_name.split(".")
    filename = txt_name_splits[0]
    return filename

def filter_file(paths):
    filtered_paths = []
    for path in paths:
        read_file = open(path, 'r')
        lines = read_file.readlines()
        if len(lines) >= 50:
            filtered_paths.append(path)
    return filtered_paths

# ファイルを初期化する
def reset_file(file_path):
    write_file = open(file_path, 'w')
    write_file.write('')
<<<<<<< HEAD
=======

    # Macの濁音問題を直す
def normalize_unicode_nfc(word):
    word_unicode_nfd = word.decode('utf-8') # strからunicode(NFD)に変換
    word_unicode_nfc = unicodedata.normalize("NFC", word_unicode_nfd) # unicode(NFD)からunicode(NFC)に変換
    word_utf8 = word_unicode_nfc.encode('utf-8') # unicode to utf-8(str)
    return word_utf8

def export_line_len_csv(line_len, onomatope, write_filename):
    write_file = open(write_filename, 'a')
    write_str = onomatope+", "+str(line_len)+"\n"
    write_file.write(write_str)

>>>>>>> a81e408aa4993ed353759e22942eda6079ee5213
#メイン。指定されたファイルをdef mainにかけて、結果をprintする。
#この結果をリダイレクトしてcsvを生成していた。
if __name__ == '__main__':
    main()
