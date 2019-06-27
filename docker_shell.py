#!/usr/bin/python2

import cgi
import commands

print "content-type: text/html"
print

print """
<script>
function change(output)
{	document.getElementById('tb2').value=output
	document.location="http://192.168.43.123/scripts/docker_shell.py?x="+data+"";
	 

}
</script>
"""
os_name = cgi.FormContent()['x'][0]
print os_name

print """
<form >
<textarea id='tb1' cols='50' rows='30' name='code' >
</textarea>
<textarea id='tb2' cols='50' rows='30' name='output'>
</textarea>
<input id='ip1' type = 'button' value='" + {0} + "' onclick= change(output) />
</form>
""".format(os_name)

data= commands.getoutput("docker exec {} {}".format(osname,code))
print data

