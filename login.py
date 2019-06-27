#!/usr/bin/python2

import cgi
import commands

print "content-type: text/html"

username =  cgi.FormContent()['username'][0]
password =  cgi.FormContent()['password'][0]



if username=='Divyansh' and password=='redhat':
	print "location: ../menu.html"
	print
else:
	print "location: ../login_.html"
	print
