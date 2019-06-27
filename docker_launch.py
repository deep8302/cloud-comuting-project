#!/usr/bin/python2

import cgi
import commands

print "content-type: text/html"
print

imageName=cgi.FormContent()['image_name'][0]
cName = cgi.FormContent()['cname'][0]

check_status = commands.getstatusoutput("sudo docker inspect {}".format(cName))

if check_status[0]==0:
	print "{}: Container name already exists ... ".format(cName)
else:
	commands.getoutput("sudo docker run -dit --name {0} {1}".format(cName,imageName))
	print "{}: container launched ..".format(cName)
	print "<a href=docker_manage.py>Click here to manage container</a>"

