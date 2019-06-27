#!/usr/bin/python2

import cgi
import commands

print "content-type: text/html"

number = cgi.FormContent()['numb'][0]
image = cgi.FormContent()['image_name'][0]
user = cgi.FormContent()['username'][0]
i = 1

while i<=int(number):
	ip = "192.168.43.123"
	commands.getstatusoutput("sshpass -p redhat ssh -o stricthostkeychecking=no -l root {0} docker run -dit --name {3}_{1} {2}".format(ip,i,image,user))
	i = i+1
print "location: docker_manage.py"
print
