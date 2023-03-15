#### CIDR
- CIDR stands for Classless Inter-Domain Routing, a method for allocating IP addresses and for IP routing .
- CIDR replaces the previous classful network addressing architecture on the Internet, which was based on fixed classes A, B and C .
- CIDR allows blocks of IP addresses to be grouped into single routing table entries, which reduces the size and complexity of routing tables and improves the efficiency of address distribution  .
- CIDR notation is a compact representation of an IP address and its associated routing prefix. It consists of an IP address followed by a slash (/) and a number, called the prefix length, which indicates the number of bits in the network portion of the address .
- For example, 192.168.1.0/24 is a CIDR notation for a block of 256 IP addresses, from 192.168.1.0 to 192.168.1.255, where the first 24 bits are the network prefix and the last 8 bits are the host identifier.
- CIDR notation can also be used to specify a single IP address, by using a prefix length of 32. For example, 192.168.1.1/32 is equivalent to 192.168.1.1.
- CIDR notation is widely used in network configuration, routing protocols, firewall rules, and access control lists .