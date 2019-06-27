#!/usr/bin/python2

import docker_images_list

print "<h2>Launch your container: </h2>"
print "<form action='docker_launch.py'>"
print "Select your docker image"
docker_images_list.docker_list()
print """
<br/>
Enter your container name: <input name='cname'>
 <br/>
<input type = 'submit' />
 <br/>
</form>
"""

