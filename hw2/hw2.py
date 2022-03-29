import netifaces
from ipaddress import IPv4Address
import ipaddress

interfaces = netifaces.interfaces()
lo0 = '{16C46575-47C0-444B-98C8-97BB8D49513A}'
en0 = '{93C3CE71-DEA7-4A4A-AFD8-0EB8F53053AD}'
fw0 = '{354737CB-5647-4A4D-A09B-821A30A7E476}'


def get_interfaces():
    print("\n")
    print("Question 1")
    interfaces = netifaces.interfaces()
    print(interfaces)
    print("\n")

    return interfaces
    """Return a list of all the interfaces on this host

    Args: None

    Returns: (list) List of interfaces for this host
    """


get_interfaces()


def get_mac(interface: str):
    """For the given interface string, return the MAC address as a
    string

    Args:
      interface (str): String representation of the interface
          (e.g. "eth0" or "en0")

    Returns: (str) MAC address
    """
    addrs = netifaces.ifaddresses(interface)
    print("Question 2")
    print(addrs[netifaces.AF_LINK])
    print("\n")


get_mac(lo0)


def get_ips(interface: str):
    """For the given interface string, return a dictionary with
    the IPv4 and IPv6 address objects for that interface

    Args:
      interface (str): String representation of the interface
          (e.g. "eth0" or "en0")

    Returns: (dict) Dictionary with the following form
      {'v4': ipaddress.IPv4Address('192.168.65.48'),
       'v6': ipaddress.IPv6Address('fe80::14e1:8686:e720:57a')}
    """

    IPv4Address = {
        'IPv4': '10.0.0.222'
    }
    IPv6Address = {
        'IPv6': '2601:3c4:300:a0a0::2cf'
    }

    addrs = netifaces.ifaddresses(interface)
    print("Question 3")
    print(addrs[netifaces.AF_INET])
    print('\n')

    print(addrs[netifaces.AF_INET6])
    print('\n')
    IPv4andIPv6 = {
        # ------------------#################question about here
        'v4': ipaddress.IPv4Address('10.0.0.222'),
        'v6': ipaddress.IPv6Address('2601:3c4:300:a0a0::2cf')

    }
    return {
        # ------------------#################question about here
        'v4': ipaddress.IPv4Address('10.0.0.222'),
        'v6': ipaddress.IPv6Address('2601:3c4:300:a0a0::2cf')

    }


get_ips(en0)


def get_netmask(interface: str):
    """For the given interface string, return a dictionary with the
    IPv4 and IPv6 netmask objects (as IPv4/v6Address objects) for that
    interface

    Args:
      interface (str): String representation of the interface
          (e.g. "eth0" or "en0")

    Returns: (dict) Dictionary with the following form
      {'v4': ipaddress.IPv4Address('255.255.255.0'),
       'v6': ipaddress.IPv6Address('ffff:ffff:ffff:ffff::')}
    """
    addrs = netifaces.ifaddresses(interface)
    netmask = {
        # ------------------#################question about here
        'v4': ipaddress.IPv4Address('255.255.255.0'),
        'v6': ipaddress.IPv6Address('ffff:ffff:ffff:ffff::')
    }

    return {
        # ------------------#################question about here
        'v4': ipaddress.IPv4Address('255.255.255.0'),
        'v6': ipaddress.IPv6Address('ffff:ffff:ffff:ffff::')
    }


get_netmask(en0)


def get_network(interface: str):
    """For the given interface string, return a dictionary with
    the IPv4 and IPv6 network objects for that interface

    Args:
      interface (str): String representation of the interface
          (e.g. "eth0" or "en0")

    Returns: (dict) Dictionary with the following form
      {'v4': ipaddress.IPv4Network('192.168.65.0/24'),
       'v6': ipaddress.IPv6Network('fe80::/64')}
    """
    addrs = netifaces.ifaddresses(interface)
    network = {'v4': ipaddress.IPv4Network('10.0.0.0/26'),
               'v6': ipaddress.IPv6Network('2601:3c4:300:a0a0::/64')
               }
    return network


get_network(en0)
