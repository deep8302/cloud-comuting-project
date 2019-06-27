#!/usr/bin/python2

import docker_images_list

print "<form action='automatic_launch.py'>"
print "Select your docker image"
docker_images_list.docker_list()

print """
<br />
Enter the number of containers you want to launch : <input name='numb'>
<br>
<br>
Enter the username: <input name = 'username'>
<br>
<br>
<input type = 'submit' />
 <br/>
</form>
"""

print "<a href='../pull.html'>Click here to pull any unavailable image</a>"
