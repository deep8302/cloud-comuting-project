#!/usr/bin/python2

import cgi
import commands

print "content-type: text/html"
print

print"""
<form>
<textarea cols='50' rows='10' name='code'>
</textarea>
<input type='submit' />
</form>
"""

cName = cgi.FormContent()['x'][0]


bash_status = commands.getstatusoutput("sudo docker exec {0}".format(ccmd))[1]


bash_status = commands.getstatusoutput("sudo docker rm -f {}".format(cName))
if cremove_status[0]==0:
        print "location: docker_manage.py"
        print
else:
        print "Failed to remove"
        print
"""
