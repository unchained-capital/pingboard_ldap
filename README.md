# Pingboard LDAP Integration

This is a simple script which crawls an LDAP server and mirrors the
user data to Pingboard.

## Quickstart

This script assumes you already have:

* A working Python environment
* with the Python `pip` dependency manager
* with the `virtualenv` package

Clone the repository and install all dependencies.

```
$ git clone https://github.com/unchained-capital/pingboard_ldap
$ cd pingboard_ldap
$ make
```

Now create the file `credentials.sh` at the top-level of this new
directory, using `credentials.example.sh` as a template.  You'll want
to insert your own Pingboard client ID & secret.

Now you can set up your shell's environment and run the script.

```
$ source environment.sh
$ python pingboard_ldap.py
```

