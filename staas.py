#!/usr/bin/python2

import commands
import cgi

print "content-type: text/html"

ch = cgi.FormContent()['choice'][0]
if ch == 'block':
	print "location: ../block_final.html"
	print
elif ch == 'object':
	print "location: ../object_STAAS.html"
	print
