#!/usr/bin/python2

import commands
import cgi

print "content-type: text/html"
print

commands.getstatusoutput("sudo docker run -it --name xy paas_python2")


