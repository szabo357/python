import ipaddress

net = ipaddress.ip_network('192.168.0.0/24')

# list all hosts in network.
for host in net.hosts():
    print(host)
    