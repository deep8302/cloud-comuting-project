#!/usr/bin/python2

import cgi
import os
import commands
print "content-type: text/html"
print

osname = os.environ['HTTP_COOKIE'].split('=')[1]
imagename = cgi.FormContent()['imagename'][0]
version = cgi.FormContent()['version'][0]

#print osname
#print imagename
#print version

image = commands.getstatusoutput("sudo docker commit {0} {1}:{2}".format(osname,imagename,version))
if image[0] == 0:
	print "Image {0}:{1} created ..".format(imagename,version)
else:
	print "Failed ..."
