#### CIDR
- CIDR stands for Classless Inter-Domain Routing, a method for allocating IP addresses and for IP routing .
- CIDR replaces the previous classful network addressing architecture on the Internet, which was based on fixed-length network prefixes.
- CIDR allows blocks of IP addresses to be grouped into single routing table entries, which reduces the size and complexity of routing tables on routers across the Internet .
- CIDR also enables more efficient use of the available IP address space, especially for IPv4, which has been exhausted since 2011.
- CIDR notation is a compact representation of an IP address and its associated routing prefix. It consists of an IP address, a slash (/), and a number that indicates the length of the prefix in bits .
- For example, 192.168.1.0/24 is a CIDR notation that represents the IP address 192.168.1.0 and its prefix of 24 bits, which corresponds to the network mask 255.255.255.0. This means that the network has 256 possible host addresses, from 192.168.1.0 to 192.168.1.255.
- CIDR notation can also be used to specify a range of IP addresses, by using a hyphen (-) to indicate the lower and upper bounds of the range. For example, 192.168.1.0-192.168.1.255/24 is equivalent to 192.168.1.0/24.
- CIDR notation is widely used in network configuration, routing protocols, firewall rules, and access control lists .