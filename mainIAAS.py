#!/usr/bin/python2

import cgi
import commands

print "content-type: text/html"





osname=cgi.FormContent()['osname'][0]
ramsize=cgi.FormContent()['ramsize'][0]
ostype=cgi.FormContent()['ostype'][0]
storage=cgi.FormContent()['storage'][0]
nocpu=cgi.FormContent()['nocpu'][0]
port=int(cgi.FormContent()['port'][0])

print "set-cookie:x={}".format(port)
print


virtset="""
---
- name: manage libvirt guests
  user: root
  hosts: iaas

  tasks:
      - name: start libvirtd
        service: name=libvirtd state=started enabled=yes
        register: libvirtd


      - name: create vm
        command : " sudo virt-install  --name {0}   --memory  {1}   --disk /var/lib/libvirt/images/{0}.qcow2,size={3}  --vcpu   {4}   --location /os/rhel-server-7.3-x86_64-dvd.iso    --os-variant  rhel7   --graphics vnc,listen=0.0.0.0,port={5}  --os-type  linux  --noautoconsole "
""".format(osname,ramsize,ostype,storage,nocpu,port) 


fh=open("vml.yml","w")
fh.write(virtset)
fh.close()



cmdStd=commands.getstatusoutput("sudo ansible-playbook vml.yml -i ../ansible/hosts")
if cmdStd[0]==0:
	print "OS lauch sucessfully"
	print "<br />"
	print "<a href = 'iaas_manage.py'>CLick here to manage OS</a>"
else:
	print "error"
                                                                                         
