# Unit 3 - IOT Data Link Layer & Network Layer Protocols

### CARP

- CARP stands for Common Address Redundancy Protocol.
- It is a protocol that allows multiple hosts on the same local network to share a set of IP addresses.
- Its main purpose is to provide redundancy and failover capabilities for IP-based services.
- CARP works by having a group of hosts on the same network segment share a virtual IP address.
- One host is designated as the master and is responsible for responding to ARP requests for the virtual IP address.
- If the master fails, another host in the group takes over as the master and begins responding to ARP requests.
- This allows for seamless failover and redundancy for IP-based services.
- CARP is commonly used in firewalls, routers, and load balancers to provide high availability and failover capabilities.
- It is an open standard and is available on many operating systems, including FreeBSD, OpenBSD, and Linux.
