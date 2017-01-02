# Hardened Edition
Builds upon the `base` role and adds additional server hardening including:

* [ ]*Potentially* use `vault` as opposed to plaintext storage per
[docs](http://docs.ansible.com/ansible/playbooks_vault.html).
* [ ] Create ssh keys using `ssh_key_passphrase` with the
    [User Module](http://docs.ansible.com/ansible/user_module.html).
* [ ] Install `cracklib` to improve PAM security
    * [ ] Password must be a minimum of 15 characters
    * [ ] New password must:
        * differ from old one by 5 characters;
        * contain at least:
            * 1 uppercase;
            * 2 lowercase;
            * 1 digit; and
            * 1 symbol.
* [ ] Disable sudo without password
* [ ] Disable the root account's user login
* [ ] Google Authenticator (2FA) for any SSH users and forced application
* [ ] IDS and notifications with Monit
* [ ] Implement [pass](https://www.passwordstore.org) for storing local data.

### TODO
Once role completed, merge back into `base` to keep code cleaner and more
concise. Given this ***should*** be best practice let's force it to be. 
