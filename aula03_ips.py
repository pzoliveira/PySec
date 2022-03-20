import ipaddress

if __name__ == '__main__':
    ipstr = '192.168.0.1'
    ipaddr = ipaddress.ip_address(ipstr)
    print(ipaddr + 2000)
    ntstr = '192.168.0.100/24'
    ntaddr = ipaddress.ip_network(ntstr, strict=False)
    print(ntaddr)
    for addr in ntaddr:
        print(addr)
