#!/usr/bin/python2

import commands
import cgi

print "content-type: text/html"

choice = cgi.FormContent()['choice'][0]



if choice == 'caas':
	print "location: automatic.py"
	print 
elif choice == 'staas':
	print "location: ../staas.html"
	print
elif choice == 'iaas':
	print "location: iaas_manage.py"
	print
