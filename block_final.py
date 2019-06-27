#!/usr/bin/python2

import commands
import cgi

print "Content-Type: text/html"
print

clientIp=cgi.FormContent()['clientip'][0]
passwd=cgi.FormContent()['password'][0]
s=cgi.FormContent()['size'][0]
lvname=cgi.FormContent()['lvname'][0]
print clientIp
print passwd
print s
Host="""[client]\n{0} ansible_ssh_user=root ansible_ssh_pass={1}\n""".format(clientIp,passwd)
#print Host

fh=open('../ansible/hosts', 'a')
fh.write(Host)
fh.close()
#print Host

vgname="cloudvg"
#print Host
#print createBlockStorage

createBlockStorage= """
---
- hosts: web
  tasks:
      - lvol:
          size: {0}
          vg: "cloudvg"
          lv:  "{1}"
      - lineinfile:
          path: "/etc/tgt/targets.conf"
          line: "<target user>"
          state: present
      - lineinfile:
          path: "/etc/tgt/targets.conf"    
          line: "backing-store /dev/cloudvg/{1}"
          state: present
      - lineinfile:
          path: "/etc/tgt/targets.conf"    
          line: "</target>"
          state: present
      - command: "setenforce 0"
      - command: "iptables -F"
      - service:
          name: "tgtd"
          state: restarted

""".format(s,lvname)

#print createBlockStorage

fh=open('../ansible/lvBcreate.yaml', 'w')
fh.write(createBlockStorage)
fh.close()

print commands.getstatusoutput("sudo ansible-playbook ../ansible/lvBcreate.yaml -i  ../ansible/hosts")
#print storageStatus


