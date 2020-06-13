import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_default_epel(host):
    r = host.file('/etc/yum.repos.d/epel.repo')
    assert r.is_file
