# Ansible role: EPEL

![Molecule Test](https://github.com/crgwilson/ansible-role-epel/workflows/Molecule%20Test/badge.svg)

Install the extra packages for enterprise linux repo

## Variables

Theres only one variable for this role, and thats the name of the package which installs the epel repo. Theres no reason to ever have to tweak it.

## Testing

Testing for this project is setup using [Molecule](https://molecule.readthedocs.io/en/stable/) & [Docker](https://www.docker.com/).
Unit tests can be run using the below command:

```console
foo@bar:~$ molecule test --all
```
