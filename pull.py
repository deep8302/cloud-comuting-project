#!/usr/bin/python2

import cgi
import commands

print "content-type: text/html"
print

os =  cgi.FormContent()['image'][0]
version = cgi.FormContent()['version'][0]

ip = "192.168.43.123"

status = commands.getstatusoutput("sshpass -p redhat ssh -o stricthostkeychecking=no -l root {2} sudo docker pull {0}:{1}".format(os,version,ip))

if status[0]==0:
	print "The image has been pulled"
	print "<a href = 'scripts/automatic.py'>Click here to use it ..</a>"
else:
	print "Failed to pull the image .."
