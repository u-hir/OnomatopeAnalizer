#!/usr/bin/env python
# -*- coding:utf-8 -*-

import cgi
import csv
import sys

def htmlprint(f):
    html_body = u"""
    <html>
    <head>
    <meta http-equiv="content-type" content="text/html; charset=utf-8">
    </head>
    <body>
    <title>オノマトペ辞書精錬</title>
    <h2>オノマトペ精錬プログラム</h2>
    <p><strong>例：「雨がざあざあ降る」</strong>のように、共に使うことのあるオノマトペと単語の組み合わせにチェックを入れて下さい。</p>
    <form action="/cgi-bin/csv_createv2.py" method="POST">
    %s
    <input type="submit" name="csv_create">
    </form>
    </br>
    </br>
    </br>
    </br>
    </br>
    <script type="text/javascript" src="ajax.js"></script>
    </body>
    </html>"""
    
    content = ''
    content += "オノマトペ：<strong >%s</strong> <br />" % form.getvalue('onomatope', '')
    content += "<input type='hidden' name='onomatope_ppp' value='%s'>" % form.getvalue('onomatope', '')
    
    for line in f.readlines():
        sentence = ''
        word = line.split(',')[0]
        speech = line.split(',')[2]

        if '名詞' in speech:
            sentence = speech + "　" + word + ' / '  + filename
        elif '動詞' in speech:
            sentence = filename + ' / ' + word + "　" + speech
        elif '形容詞' in speech:
            sentence = speech + "　" + word + ' / '  + filename
        elif '副詞' in speech:
            sentence = speech + "　" + word + ' / '  + filename
            
        content += "<p>　<input type='checkbox' name='check' value='" + word + "'>　" + sentence + "</p>"

    content = content.decode("utf-8")

    print (html_body % content).encode('utf-8')


form = cgi.FieldStorage()

filename = form.getvalue(u"onomatope", '')

print "Content-type: text/html\n"

file = open("output/" + filename + ".csv", "r")
htmlprint(file)

