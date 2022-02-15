import netifaces
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
    addrs = netifaces.ifaddresses(interface)
    Ip_dic = {}
    # print("Question 3")

    try:
        addrs[netifaces.AF_INET][0]['addr']
        ipAdr6_15 = addrs[netifaces.AF_INET6][0]['addr']
        ipAdr6 = ipAdr6_15[0: ipAdr6_15.index('%')]

        print(interface + " have addr")
        print('\n')
        Ip_dic = {

            'v4_ad': ipaddress.IPv4Address(addrs[netifaces.AF_INET][0]['addr']),
            'v6_ad': ipaddress.IPv6Address(ipAdr6),

        }
        print(Ip_dic)
    except:
        print(interface + "don't have addr")
        print("")

    return Ip_dic


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
    Ip_dic = {}
    addrs = netifaces.ifaddresses(interface)

    try:
        addrs[netifaces.AF_INET][0]['netmask']

        ip6Net_sl = addrs[netifaces.AF_INET6][0]['netmask']
        ip6Net = ip6Net_sl[0: ip6Net_sl.index('/')]
        # print(ip6Net)
        print(interface + " have a netmask")
        Ip_dic = {
            # ------------------#################question about here
            'v4_netmask': ipaddress.IPv4Address(addrs[netifaces.AF_INET][0]['netmask']),
            'v6_netmask': ipaddress.IPv6Address(ip6Net)
        }
        print(Ip_dic)
        print("")
    except:
        print(interface + "don't have netmask")
        print("")

    return Ip_dic


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
    Ip_dic = {}
    addrs = netifaces.ifaddresses(interface)

    try:
        # if interface has no address, network does not exist too.s
        addrs[netifaces.AF_INET][0]['addr']

        ipAdr6_15 = addrs[netifaces.AF_INET6][0]['addr']
        ip6Net = ipAdr6_15[0: ipAdr6_15.index('%')]

        Ip_dic = {
            'v4_network': ipaddress.ip_address(addrs[netifaces.AF_INET][0]['addr']),
            'v6_network': ipaddress.ip_address(ip6Net)
        }
        print(interface + " have a network")
        print(Ip_dic)
        print("")
    except:
        print(interface + "don't have network")
        # print(addrs[netifaces.AF_INET6])
    return Ip_dic


get_network(en0)

for i in get_interfaces():
    get_ips(i)
    get_netmask(i)
    get_network(i)

# print(answer)
# if(answer == True):
#     try:
#         get_ips(i)

#     except:
#         print('error')
