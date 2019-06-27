#!/usr/bin/python2

import commands
import cgi

print "content-type: text/html"



cName = cgi.FormContent()['x'][0]


cstart=commands.getstatusoutput("sudo sshpass -p redhat ssh -o stricthostkeychecking=no -l root 192.168.43.222 virsh start {}".format(cName))

if cstart[0]==0:
        print "location: iaas_manage.py"
        print
else:
        print "Failed to start"
        print
