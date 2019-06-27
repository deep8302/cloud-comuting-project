#!/usr/bin/python2

import commands
import cgi

print "content-type: text/html"
"""
<script>
function lw(mycname)
{
document.location = 'docker_commit.py?x=' + mycname
}
</script>
"""

container_name =  cgi.FormContent()['cn'][0]
options = cgi.FormContent()['options']

print "set-cookie: x = {}".format(container_name)
print

ip = commands.getoutput("sudo docker inspect {0} | jq '.[].NetworkSettings.Networks.bridge.IPAddress'".format(container_name)).strip('"')

for i in options:
        if i=='web-server':
		print "web"
		c = commands.getstatusoutput("sudo docker exec {} rpm -q httpd".format(container_name))
		if c[0] == 0:
			print "{} already exists ...<br>".format(i)
		else:
			print "Installing your {} ...<br>".format(i)
			commands.getstatusoutput("sudo docker exec {} yum install httpd".format(container_name))
		d = commands.getstatusoutput("sudo docker exec {} /usr/sbin/httpd".format(container_name))
		if d[0] == 0:
			print "Http service started\n"
		else:
			print "Failed to start the HTTP service\n"
	elif i=='ssh-server':
		c1 = commands.getstatusoutput("sudo docker exec {} rpm -q openssh-server".format(container_name))
                if c1[0] == 0:
			print "{} already exists ...<br>".format(i)
                else:
                        print "Installing your {} ...<br>".format(i)
                        commands.getstatusoutput("sudo docker exec {} yum install openssh-server".format(container_name))
                d1 = commands.getstatusoutput("sudo docker exec {} /usr/sbin/sshd".format(container_name))
                if d1[0] == 0:
                        print "SSH service started\n"
                else:
                        print "Failed to start SSH service\n"
	elif i=='php':
		c2 = commands.getstatusoutput("sudo docker exec {} rpm -q php".format(container_name))
                if c2[0] == 0:
                        print "{} already exists ...<br>".format(container_name)
                else:
                        print "Installing your {} ...<br>".format(container_name)
                        commands.getstatusoutput("sudo docker exec {} yum install php".format(container_name))
	elif i=='nfs-server':
		c3 = commands.getstatusoutput("sudo docker exec {} rpm -q nfs-utils".format(container_name))
                if c3[0] == 0:
                        print "{} already exists ...<br>".format(container_name)
                else:
                        print "Installing your {} ...<br>".format(container_name)
                        commands.getstatusoutput("sudo docker exec {} yum install nfs-utils".format(container_name))
                d3 = commands.getstatusoutput("sudo docker exec {} /usr/sbin/nfsd".format(container_name))
                if d3[0] == 0:
                        print "SSH service started<br>"
                else:
			print "Failed to start the service ..<br>"
print "<br>"
print "<a href = 'docker_commit.py'> click here to commit your image </a>"
#print "<input type = 'button' value = '" + container_name + "' onclick = lw(this.value) />"
