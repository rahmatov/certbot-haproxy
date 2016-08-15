"""HAProxy plugin constants."""
from certbot import util

CLI_DEFAULTS_DEBIAN_JESSIE = dict(
    server_root="/etc/haproxy",
    version_cmd=['haproxy', '-v'],
    restart_cmd=['sudo', 'systemctl', 'restart', 'haproxy'],
    # Needs the config file as an argument:
    conftest_cmd=['/usr/sbin/haproxy', '-c', '-f'],
    haproxy_config="/etc/haproxy/haproxy.cfg",
    crt_directory="/etc/ssl/crt/",
)

CLI_DEFAULTS_DEBIAN_WHEEZY = dict(
    server_root="/etc/haproxy",
    version_cmd=['haproxy', '-v'],
    restart_cmd=['service', 'haproxy', 'restart'],
    # Needs the config file as an argument:
    conftest_cmd=['/usr/sbin/haproxy', '-c', '-f'],
    haproxy_config="/etc/haproxy/haproxy.cfg",
    crt_directory="/etc/ssl/crt/",
)

CLI_DEFAULTS = {
    "debian": CLI_DEFAULTS_DEBIAN_JESSIE,
    "debian:jessie": CLI_DEFAULTS_DEBIAN_JESSIE,
    "debian:wheezy": CLI_DEFAULTS_DEBIAN_WHEEZY,
    "ubuntu": CLI_DEFAULTS_DEBIAN_WHEEZY
}


def os_constant(key):
    """Get a constant value for operating system
    :param key: name of cli constant
    :return: value of constant for active os
    """
    os_info = util.get_os_info()
    try:
        constants = CLI_DEFAULTS[os_info[0].lower()]
    except KeyError:
        constants = CLI_DEFAULTS["debian"]
    return constants[key]
