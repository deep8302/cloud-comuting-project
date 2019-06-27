#!/usr/bin/python2

import commands

print "content-type: text/html"
print

def docker_list():
	z = 1
	container_ip = "192.168.43.123"
	print "<select name='image_name'>"
	for i in commands.getoutput("sshpass -p redhat ssh -o stricthostkeychecking=no -l root {} sudo docker images".format(container_ip)).split('\n'):
		if z<4:
			z = z+1
			pass
		else:
			j = i.split()
			print "<option>{0}:{1}</option>".format(j[0],j[1])
	print "</select>"
