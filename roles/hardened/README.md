# Hardened Edition
Builds upon the `base` role and adds additional server hardening including:

* [x] Increase security levels of SSH using appropriate Ciphers, MACs and Keys
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
* [x] Disable sudo without password
* [x] Disable the root account's user login
* [ ] Google Authenticator (2FA) for any SSH users and forced application
    * [ ] Fix returned QR code in line with
    [URL schema](https://github.com/google/google-authenticator/wiki/Key-Uri-Format)
* [ ] IDS and notifications with Monit
* [ ] Implement [pass](https://www.passwordstore.org) for storing local data.

## Important note
This role currently depends on the `tempfile` module which is only available
in `ansible 2.3` upwards. At time of writing this was not yet available via
pypy so installation was required using the git repo `devel` branch.
```
pip install --upgrade git+https://github.com/ansible/ansible.git
```

### TODO
Once role completed, merge back into `base` to keep code cleaner and more
concise. Given this ***should*** be best practice let's force it to be.

* [ ] Add option to use a Tor Hidden service for SSH per
    [Secure Secure Shell](https://stribika.github.io/2015/01/04/secure-secure-shell.html)
    * [ ] Yes/No
        * [ ] Pure Tor (i.e. only listen on loopback)
        * [ ] Listen on both
