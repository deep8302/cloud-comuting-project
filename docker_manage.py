#!/usr/bin/python2
import commands

print "content-type: text/html"
print

print """
<script>
function lw(mycname)
{
//alert 'hello';
document.location = 'docker_remove.py?x=' + mycname
}
function lw_start(mycname)
{
	document.location = 'docker_start.py?x=' + mycname
}
function lw_stop(mycname)
{
	document.location = 'docker_stop.py?x=' + mycname
}
function bash_start(mycname)
{
	document.location = 'docker_bash.py?x=' + mycname
}
</script>
"""

z = 1
ip = "192.168.43.123"
print "<table border='5'>"
print "<tr><th>Image Name</th><th>ContainerName</th><th>Status</th><th>IP_Address</th><th>Stop</th><th>Start</th><th>Remove</th><th>Bash</th></tr>"
for i in commands.getoutput("sshpass -p redhat ssh -o stricthostkeychecking=no -l root {} sudo docker ps -a".format(ip)).split('\n'):
	if z<4:
		z = z+1
		pass
	else:
		j = i.split()
		cStatus = commands.getoutput("sudo docker inspect {0} | jq '.[].State.Status'".format(j[-1]))
		print_status = commands.getoutput("sudo docker inspect {0} | jq '.[].NetworkSettings.Networks.bridge.IPAddress'".format(j[-1]))

		print "<tr><td>" + j[1] + "</td><td> " + j[-1] + "</td><td>{0}</td><td>{1}</td><td  align=\"center\"><input type='button' value='".format(cStatus,print_status) + j[-1] + "' onclick = lw_stop(this.value) /></td><td align=\"center\"><input type='button' value = '" + j[-1] + "'onclick = lw_start(this.value) /></td><td align=\"center\"><input type='button' value ='" + j[-1]+"' onclick = lw(this.value) /></td><td><input type = 'button' value='" + j[-1] + "' onclick= bash_start(this.value) /></td></tr>"
print "</table>"
print "<br>"
print "<a href ='../customize.html'>Click here to customize your OS</a>"

