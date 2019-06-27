#!/usr/bin/python2
import cgi

print "content-type: text/html"
print

choice= cgi.FormContent()['choice'][0]


if choice == 'python':
	print "<a href = 'PAAS_python2.py'> click here for python2</a><br />"
	print "<a href = 'PAAS_python3.'> click here for python3</a>"
elif choice == 'java':
	print "<a href=>click here for jdk_1.7</a><br />"
        print "<a href=>click here for jdk_1.8</a>"
else:
	print "not supported!!!"
