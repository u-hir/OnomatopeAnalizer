# coding: utf-8
import glob
import unicodedata

def main():
	ono_file_names = glob.glob('onolist/*.txt')
	sentence_paths = glob.glob('sentences/*.txt')

	onomatopes = []
	for ono_file_name in ono_file_names:
		ono_file = open(ono_file_name, 'r')
		onomatopes.extend(ono_file.readlines())
		ono_file.close()
	refresh_file = open('userdic.txt', 'w')
	refresh_file.write('')
   	refresh_file.close()
	for sentence_path in sentence_paths:
		file_name = get_filename(sentence_path)
		file_name = file_name.replace('\n', '')
		file_name = file_name.replace('\r', '')
		file_name_normalize = normalize_unicode_nfc(file_name)
		for i, onomatope in enumerate(onomatopes):
   	   		onomatope = onomatope.replace('\n', '')
   			onomatope = onomatope.replace('\r', '')
			onomatope_normalize = normalize_unicode_nfc(onomatope)
			if onomatope_normalize == file_name_normalize:
				onomatopes.pop(i)
			if onomatope_normalize == '':
				onomatopes.pop(i)
	for onomatope in onomatopes:
		print onomatope


def get_filename(path):
    # パスからファイル名を取得
    path_splits = path.split("/") # パスの文字列を/で区切る
    txt_name = path_splits[-1] # 最後の要素が*.txt形式のファイル名
    txt_name_splits = txt_name.split(".")
    filename = txt_name_splits[0]
    return filename

# Macの濁音問題を直す
def normalize_unicode_nfc(word):
    word_unicode_nfd = word.decode('utf-8') # strからunicode(NFD)に変換
    word_unicode_nfc = unicodedata.normalize("NFC", word_unicode_nfd) # unicode(NFD)からunicode(NFC)に変換
    word_utf8 = word_unicode_nfc.encode('utf-8') # unicode to utf-8(str)
    return word_utf8

if (__name__ == '__main__'):
	main()
