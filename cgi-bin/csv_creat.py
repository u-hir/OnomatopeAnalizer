#!/usr/bin/env python
# -*- coding:utf-8 -*-

import cgi
import csv
import sys


form = cgi.FieldStorage()

checklist = form.getlist('check')

onomatope = "しとしと"

csvfile = open(onomatope + ".csv", "w")

print "Content-Type:text/html; charset:utf-8; \n";
for item in checklist:
    print item + "</br>"

