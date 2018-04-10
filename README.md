# SSMTP

Master: [![Build Status](https://travis-ci.org/sansible/ssmtp.svg?branch=master)](https://travis-ci.org/sansible/ssmtp)  
Develop: [![Build Status](https://travis-ci.org/sansible/ssmtp.svg?branch=develop)](https://travis-ci.org/sansible/ssmtp)

* [Installation and Dependencies](#installation-and-dependencies)
* [Tags](#tags)
* [Examples](#examples)

This roles installs SSMTP.


## Installation and Dependencies

To install this role run `ansible-galaxy install sansible.ssmtp`
or add this to your `roles.yml`

```YAML
- name: sansible.ssmtp
  version: v2.0
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
      sansible_ssmtp_group: ssmtp_user
      sansible_ssmtp_user: ssmtp_user
      sansible_ssmtp_mailserver_host: localhost
      sansible_ssmtp_mailserver_password: password
      sansible_ssmtp_mailserver_port: 25
      sansible_ssmtp_mailserver_username: username
```
