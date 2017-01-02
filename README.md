# ansible-roles
A collection of `roles` for the [ansible](http://docs.ansible.com/ansible/)
automated deployment tool.

## Initial Usage Examples:
```
# Uses an (optional) ansible config file
export ANSIBLE_CONFIG=ansible.cfg && ansible-playbook -kb --ask-become-pass -i inventoryFile base.yml -vvvv
```
