#!/usr/bin/env python
# -*- coding:utf-8 -*-

import cgi
form = cgi.FieldStorage()

html_body = u"""
<html>
<head>
<meta http-equiv="content-type" content="text/html; charset=utf-8">
</head>
<body>
%s
</body>
</html>"""

content = ''
content += "Hello %s !<br />" % form.getvalue('name', '')

print "Content-type: text/html\n"
print html_body % content
