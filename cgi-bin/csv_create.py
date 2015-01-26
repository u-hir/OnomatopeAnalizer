#!/usr/bin/env python
# -*- coding:utf-8 -*-

import cgi
import csv
import sys


form = cgi.FieldStorage()

checklist = form.getlist('check')

onomatope = form['onomatope_ppp'].value

csvfile = open(onomatope + ".csv", "w")

print "Content-Type:text/html; charset:utf-8; \n";
print '<p>' + onomatope + '</p>'
for item in checklist:
    print item + "</br>"

