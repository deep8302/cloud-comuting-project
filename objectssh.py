#!/usr/bin/python2

import commands
import getpass
import cgi
import os

print "content-type: text/html"
print

print "drive created"
vgname="cloudvg"
#username=raw_input("enter the username:")
#password=getpass.getpass("enter the password:")
username="gyt"
password="redhat"
clientip=cgi.FormContent()['clientip'][0]

keydel=commands.getstatusoutput(" sudo rm -rvf /root/.ssh/known_hosts ")
if keydel[0]==0:
	print "wait"
else:
	print "error"
usercreate="""
---
- hosts : storagesystem
  tasks:
   - user :
      name : {0}    
      password : {1}
""".format(username,password)

userfile=open("useradd.yml","w")
userfile.write(usercreate)
userfile.close()

userCreSta=commands.getstatusoutput("sudo ansible-playbook useradd.yml")

if userCreSta[0]==0:
	print("user created ")
else:
	print("not created")



drivesize=cgi.FormContent()['drivesize'][0]
formattype = "ext4"
lvpath = "/dev/mapper/{0}-{1}".format(vgname,username)
mountpoint = "/cloud/{0}".format(username)

maincmd="""
---
- hosts : storagesystem

  tasks :
   - lvol :
      vg : {0}
      lv : {1}
      size : {2}

   - filesystem :
      fstype : {3}
      dev : {4}

   - mount :
      name : {5}
      src : {4}
      fstype : {3}
      state : mounted""".format(vgname,username,drivesize+'G',formattype,lvpath,mountpoint)

fh=open("lvcreate.yml",'w')
fh.write(maincmd)
fh.close()

ansSta=commands.getstatusoutput("sudo ansible-playbook lvcreate.yml")
if ansSta[0]==0:
	print("lv created and mounted")
else:
	print("lvm not created")


lineto="/dev/mapper/{1}-{0} /cloud/{0} ext4 defaults 1 2\n".format(username,vgname)
serviceCmd="""
---
- hosts : storagesystem
  tasks :
   - service:
       name : sshd 
       state : restarted

   - command : chown apache  /cloud/{0}
   - command : chmod 744  /cloud/{0}

   - lineinfile :
      path : "/etc/fstab"
      regexp : {0}
      line : {1}
""".format(username,lineto)


sshf=open("serviceSta.yml","w")
sshf.write(serviceCmd)
sshf.close()

serviceSta=commands.getstatusoutput("sudo ansible-playbook serviceSta.yml")
if serviceSta[0]==0:
	print("service started")
else:
	print("service not started")
print "drive created"



filename="/etc/ansible/client"+clientip

fh2=open(filename,"w")
string="[client{0}]\n{0}   ansible_ssh_user=root ansible_ssh_pass=redhat".format(clientip)
fh2.write(string)
fh2.close()


storageip="192.168.43.152"
createDir="""
---
- hosts : client{3}
  tasks :
  - file :
       path : "/media/{0}"
       state : directory
  - command : "chown {0} /media/{0}"
  - command : "chmod 777 /media/{0}"
  - package :
       name : "fuse-sshfs"
       state : present
  - shell : " echo  {2} | sshfs -o password_stdin,stricthostkeychecking=no  root@{1}:/cloud/{0}    /media/{0}"
""".format(username,storageip,password,clientip)

fh=open("sshfsmount.yml","w")
fh.write(createDir)
fh.close()

mountSta=commands.getstatusoutput("ansible-playbook  sshfsmount.yml  -i  /etc/ansible/{0} ".format(filename))
if mountSta[0]==0:
        print "drive is ready and mounted"
else:
        print "not done"


print "drive created"


