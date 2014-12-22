import os
import sys

def mkdir():
    filename = sys.argv[1]
    splitname = filename.split(".")
    print splitname[0]
    os.mkdir(splitname[0])

if __name__ == '__main__':
    mkdir()

#for文でスニペットを読んでファイルに書き出し
#    for 
