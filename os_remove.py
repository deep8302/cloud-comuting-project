#!/usr/bin/python2

import commands
import cgi

print "content-type: text/html"



cName = cgi.FormContent()['x'][0]



cremove_status = commands.getstatusoutput("sudo sshpass -p redhat ssh -o stricthostkeychecking=no -l root 192.168.43.222  virsh undefine {}".format(cName))
if cremove_status[0]==0:
	print "location: iaas_manage.py"
	print
else:
	print "Failed to remove"
	print

