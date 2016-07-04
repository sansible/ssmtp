# SSMTP

Master: [![Build Status](https://travis-ci.org/sansible/ssmtp.svg?branch=master)](https://travis-ci.org/sansible/ssmtp)  
Develop: [![Build Status](https://travis-ci.org/sansible/ssmtp.svg?branch=develop)](https://travis-ci.org/sansible/ssmtp)

* [ansible.cfg](#ansible-cfg)
* [Installation and Dependencies](#installation-and-dependencies)
* [Tags](#tags)
* [Examples](#examples)

This roles installs SSMTP.




## ansible.cfg

This role is designed to work with merge "hash_behaviour". Make sure your
ansible.cfg contains these settings

```INI
[defaults]
hash_behaviour = merge
```




## Installation and Dependencies

To install this role run `ansible-galaxy install sansible.ssmtp`
or add this to your `roles.yml`

```YAML
- name: sansible.ssmtp
  version: v1.0
```

and run `ansible-galaxy install -p ./roles -r roles.yml`




## Tags

This role uses two tags: **build** and **configure**

* `build` - Installation of SSMTP and dependencies.
* `configure` - SSMTP configuration files.




## Examples

To simply install SSMTP for a mailhost:

```YAML
- name: Install and configure SSMTP
  hosts: "somehost"

  roles:
    - role: sansible.ssmtp
      ssmtp:
        group: ssmtp_user
        user: ssmtp_user
        config:
          host: localhost
          password: password
          port: 25
          username: username
```
