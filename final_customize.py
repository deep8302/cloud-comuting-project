#!/usr/bin/python2

import commands
import cgi

print "content-type: text/html"
print

print """
<script>
function lw(mycname)
{
document.location = 'docker_commit.py?x=' + mycname
}
</script>
"""

container_name =  cgi.FormContent()['cn'][0]
options = cgi.FormContent()['options']
print container_name
print options

ip = commands.getoutput("sudo docker inspect {0} | jq '.[].NetworkSettings.Networks.bridge.IPAddress'".format(container_name)).strip('"')
print ip

fh = open("../ansible/host","w")
fh.write("[web]\n")
fh.write("{} ansible_ssh_user=root ansible_ssh_pass=redhat".format(ip))
fh.close()
"""
for i in options:
	if i=='web-server':
	       #print "web-server"
		print commands.getstatusoutput("sudo ansible-playbook ../ansible/web_server_configuration.yml -i ../ansible/host")
	
	if a[0]==0:
			print "done..."
		else:
			print "not done ..."
	elif i=='php':
		print 'php'
		a = commands.getstatusoutput("sudo ansible-playbook ../ansible/php.yml -i ../ansible/host")
                if a[0]==0:
                        print "done..."
                else:
                        print "not done ..."
	elif i=='nfs-server':
		print "nfs-server"
		commands.getstatusoutput("sudo ansible-playbook ../ansible/nfs_configuration.yml -i ../ansible/hosts")
	elif i=='ssh-server':
		print "ssh-server"
		commands.getstatusoutput("sudo ansible-playbook ../ansible/ssh_configuration.yml -i ../ansible/hosts")

print "<br /><br /><input type = 'button' value='" + container_name + "' onclick= lw(this.value) />"
"""
