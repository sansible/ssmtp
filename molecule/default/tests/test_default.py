import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_users(host):
    assert host.user('ssmtp_user').group == 'ssmtp_group'


def test_packages(host):
    assert host.package('ssmtp').is_installed


def test_files(host):
    ssmtp_exe = host.file('/usr/sbin/ssmtp')
    assert ssmtp_exe.user == 'ssmtp_user'
    assert ssmtp_exe.group == 'ssmtp_group'
    assert ssmtp_exe.mode == 0o770

    with host.sudo('ssmtp_user'):
        revaliases = host.file('/etc/ssmtp/revaliases').content_string
        assert 'ssmtp_user:john_doe:localhost:25' in revaliases

        ssmtp_conf = host.file('/etc/ssmtp/ssmtp.conf').content_string
        assert 'AuthUser=john_doe' in ssmtp_conf
        assert 'AuthPass=swordfish' in ssmtp_conf
