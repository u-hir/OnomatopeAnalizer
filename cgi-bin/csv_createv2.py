#!/usr/bin/env python
# -*- coding:utf-8 -*-

import cgi
import csv
import sys


form = cgi.FieldStorage()

checklist = form.getlist('check')

onomatope = form['onomatope_ppp'].value

csvReader = csv.reader(open("cgi-bin/RefiningOutputs/"+ onomatope + ".csv", "rb"),delimiter='', quoterchar='|')
print csvReader

print "Content-Type:text/html; charset:utf-8; \n";
print '<p>' + onomatope + '</p>'
for item in checklist:
    print item + ",1</br>"
    csvfile.write(item + ",1\n")
csvfile.close()
