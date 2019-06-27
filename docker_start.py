#!/usr/bin/python2

import commands
import cgi

print "content-type: text/html"


ip = "192.168.43.123"
cName = cgi.FormContent()['x'][0]


cstart=commands.getstatusoutput("sshpass -p \"redhat\" ssh -o stricthostkeychecking=no -l root 192.168.43.123 sudo docker start {}".format(cName))

if cstart[0]==0:
        print "location: docker_manage.py"
        print
else:
        print "Failed to start"
        print
