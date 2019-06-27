#!/usr/bin/python2
import commands

print "content-type: text/html"
print



print """
<script>
function lw_remove(mycname)
{
//alert 'hello';
document.location = 'os_remove.py?x=' + mycname
}
function lw_start(mycname)
{
	document.location = 'os_start.py?x=' + mycname
}
function lw_stop(mycname)
{
	document.location = 'os_stop.py?x=' + mycname
}

</script>
"""

print "<a href ='../form.html'>Click here to customize your OS</a>"
z = 0
#ip = "192.168.43.123"
print "<table border='5'>"
print "<tr><th>Id</th><th>Name</th><th>Status</th><th>Stop</th><th>Start</th><th>Remove</th></tr>"
for i in commands.getoutput("sudo sshpass -p redhat ssh -o stricthostkeychecking=no -l root 192.168.43.222 virsh list --all").split('\n'):
	if z<2:
		z = z+1
		pass
	else:
		j = i.split()
		print "<tr><td>" + j[0] + "</td><td> " + j[1] + "</td><td>"+j[2]+"</td><td  align=\"center\"><input type='button' value='" + j[1] + "' onclick = lw_stop(this.value) /></td><td align=\"center\"><input type='button' value = '" + j[1] + "'onclick = lw_start(this.value) /></td><td align=\"center\"><input type='button' value ='" + j[1]+"' onclick = lw_remove(this.value) /></td></tr>"
print "</table>"
print "<br />"

#print "mhit"
#print "<a href ='../customize.html'>Click here to customize your OS</a>"

