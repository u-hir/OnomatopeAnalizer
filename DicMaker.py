# coding: utf-8
import glob
import re
import commands

def main():
	ono_file_names = glob.glob('onolist/*.txt')
	lines = []
	for ono_file_name in ono_file_names:
		ono_file = open(ono_file_name, 'r')
		lines.extend(ono_file.readlines())
		ono_file.close()
	refresh_file = open('userdic.txt', 'w')
	refresh_file.write('')
   	refresh_file.close()
	for line in lines:
   	   	line = line.replace('\n', '')
   		line = line.replace('\r', '')
   		
		output_file = open('userdic.txt', 'a')
		dic_line = line+",-1,-1,0,副詞,一般,*,*,*,*,"+line+","+line+",オノマトペ\n"
		print(dic_line)
		output_file.write(dic_line)
	output_file.close()	
	commands.getoutput("/opt/local/libexec/mecab/mecab-dict-index -d /opt/local/lib/mecab/dic/ipadic-utf8 -u userdic.dic -f utf-8 -t utf-8 userdic.txt")


if (__name__ == '__main__'):
	main()
