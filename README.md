# ansible-roles
A collection of `roles` for the [ansible](http://docs.ansible.com/ansible/)
automated deployment tool.

This repository for roles follows the [best practices for content organisation](http://docs.ansible.com/ansible/playbooks_best_practices.html#content-organization) as detailed by the official guidance wherever possible.

Directory structure as follows:
```bash
ansible-roles
    +- deploy
        |- log
        |    \- ansible.log  <-- logfile output if using `ansible.cfg`
        |- password  <-- auto-created passwords for users
        |    \- hostname1
        |       |- adminlocal.txt
        |       \- user1.txt
        \- ssh  <-- auto-created ssh keys for users
            \- hostname1
                |- ansible.id_rsa
                \- ansible.id_rsa.pub
    |- examples
        \- base.yml  <-- example playbook
    \- roles
        |- base
        \- ...
```

## Initial Usage Examples:
```
# Uses an (optional) ansible config file
export ANSIBLE_CONFIG=ansible.cfg && ansible-playbook -kb --ask-become-pass -i inventoryFile base.yml -vvvv
```
