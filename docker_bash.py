#!/usr/bin/python2

import cgi
import commands

print "content-type: text/html"
print

osname =  cgi.FormContent()['x'][0]

status = commands.getstatusoutput("sudo docker inspect {0} | jq '.[].NetworkSettings.Networks.bridge.IPAddress'".format(osname))
ip = status[1].strip('"')
"""print ip
if status[0]==0:
	print "Ok"
else:
	print "Not ok"
"""
print "<iframe src = http://{0}:4200 width = '400' height = '300'></iframe>".format(ip)
