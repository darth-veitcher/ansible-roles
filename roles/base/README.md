# ansible-base
Basic install and setup of Ubuntu Server. Tested on 16.04.1 LTS

## Intro
This is an automated (semi) ansible role designed to deploy and configure an
Ubuntu Server 16.04 LTS into a base vanilla state with some security measures.

It may work on other platforms but has not been tested.

As an added benefit it has the `ssh_setup.yml` task file which will check for
a valid ssh connection and, based on results, load up the new parameters after
we have locked down and changed ports. This saves us from needing to constantly
change the inventory file.

## Base.yml
A standard playbook usage would contain the following - note the usage of a
section to prep the server for ansible requirements. This is only really for
the `base` role as we assume that everything going forwards already has ansible
setup properly.

It then continues with the role install.

```
---
# file: base.yml
# Need gather_facts and pre_tasks to bootstrap python2 requirements on default
# Ubuntu install when >= 15.04
# http://stackoverflow.com/a/34402816
- hosts: all
  gather_facts: no
  environment:
    ANSIBLE_HOST_KEY_CHECKING: False
  pre_tasks:
    - include: roles/ansible-base/tasks/ssh_setup.yml
    - name: install python2
      raw: sudo apt-get -y install python-simplejson
  roles:
    - base
```

### Ansible notes
```
# Initial sysprep via SSH for ansible commands
# You could do this as opposed to the pre_tasks prep section in the playbook
echo "sudo apt-get update && sudo apt-get install software-properties-common python2.7 python-apt -y" > /tmp/installer.sh
MYCOMMAND=$(base64 /tmp/installer.sh)
ssh -t adminlocal@ "echo $MYCOMMAND | base64 -d | sudo bash"
```
