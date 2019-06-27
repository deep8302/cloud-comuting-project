#!/usr/bin/python2

import cgi
import commands
import os

print "content-type: text/html"
print

"""
<script>
function lw(os,image)
{
document.location = 'docker_commit1.py?x=' + os + '&y=' + image
}
</script>
"""

#osname = os.environ['HTTP_COOKIE']


print """
<form action = 'docker_commit1.py'>
Enter the image name that you want to give <input type = 'text' name = 'imagename'><br>
Enter the version <input type = 'text' name = 'version' />
<br>
<input type = 'submit' />
<br>
</form>
"""


